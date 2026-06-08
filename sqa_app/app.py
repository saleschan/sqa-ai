import streamlit as st
import requests
import re
import zipfile
import io
from groq import Groq

st.set_page_config(
    page_title="SQA Tool – LibreOffice",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🔬 SQA Tool — LibreOffice × IA")
st.caption("Framework de Garantia de Qualidade · FATEC Cotia 2026")
st.divider()

# ── API Key ───────────────────────────────────────────────────────────────────
if "api_key" not in st.session_state:
    st.info("Configure sua **Groq API Key** para começar. É gratuita em [console.groq.com](https://console.groq.com).")
    col1, col2 = st.columns([4, 1])
    with col1:
        key = st.text_input("API Key", type="password", placeholder="gsk_...", label_visibility="collapsed")
    with col2:
        if st.button("Salvar", type="primary", use_container_width=True) and key:
            st.session_state["api_key"] = key
            st.rerun()
    st.stop()

# ── Tags ──────────────────────────────────────────────────────────────────────
ANALYSIS_TAGS = [
    ("1 · Planejamento",    "KPIs e plano de SQA"),
    ("2 · Requisitos",      "Ambiguidades e lacunas"),
    ("3 · Arquitetura",     "Acoplamento e complexidade"),
    ("4 · Desenvolvimento", "Padrões inseguros e análise estática"),
    ("5 · Testes",          "Cobertura, regressão e fuzzing"),
    ("6 · CI/CD",           "Pipeline, build e monitoramento"),
    ("7 · Defeitos",        "Triagem e duplicatas"),
    ("8 · Feedback",        "Usabilidade e UX"),
    ("9 · Documentação",    "Doxygen e onboarding"),
    ("10 · Governança",     "Licenças, segurança e WCAG 2.1"),
    ("11 · Lançamento",     "Crash reports e telemetria"),
]

CODE_EXTS = (".cpp", ".cxx", ".c", ".h", ".hpp", ".py", ".java", ".cs", ".ts", ".js", ".svelte", ".vue", ".jsx", ".tsx", ".html", ".css", ".scss", ".go", ".rb", ".php", ".kt", ".swift")

# ── Helpers ───────────────────────────────────────────────────────────────────
def stream_response(prompt: str):
    client = Groq(api_key=st.session_state["api_key"])
    placeholder = st.empty()
    full = ""
    with client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=3000,
        stream=True,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for chunk in stream:
            full += chunk.choices[0].delta.content or ""
            placeholder.markdown(full + "▌")
    placeholder.markdown(full)


def fetch_raw(url: str) -> str:
    gh = re.match(r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)", url)
    if gh:
        u, r, b, p = gh.groups()
        url = f"https://raw.githubusercontent.com/{u}/{r}/{b}/{p}"
    gl = re.match(r"https://gitlab\.com/([^/]+/[^/]+)/-/blob/([^/]+)/(.+)", url)
    if gl:
        proj, b, p = gl.groups()
        url = f"https://gitlab.com/{proj}/-/raw/{b}/{p}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.text


def github_file_list(repo_url: str) -> tuple[list[str], dict]:
    """Returns (file_list, meta) where meta has user/repo/branch for later fetching."""
    gh = re.match(r"https://github\.com/([^/]+)/([^/\s?#]+)", repo_url.strip())
    if not gh:
        return [], {"erro": f"URL não reconhecida: {repo_url}"}
    user, repo = gh.group(1), gh.group(2).removesuffix(".git")

    info = requests.get(f"https://api.github.com/repos/{user}/{repo}", timeout=10)
    if info.status_code != 200:
        return [], {"erro": f"Repositório não encontrado ({info.status_code})"}
    branch = info.json().get("default_branch", "main")

    r = requests.get(f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}?recursive=1", timeout=10)
    if r.status_code != 200:
        return [], {"erro": f"Trees API retornou {r.status_code}"}
    files = [
        f["path"] for f in r.json().get("tree", [])
        if f["type"] == "blob" and any(f["path"].endswith(e) for e in CODE_EXTS)
    ]
    return sorted(files)[:300], {"user": user, "repo": repo, "branch": branch}


def files_from_zip(uploaded) -> dict[str, str]:
    result = {}
    with zipfile.ZipFile(io.BytesIO(uploaded.read())) as zf:
        for name in zf.namelist():
            if any(name.endswith(e) for e in CODE_EXTS) and not name.startswith("__"):
                try:
                    result[name] = zf.read(name).decode("utf-8", errors="ignore")
                except Exception:
                    pass
    return result


def build_prompt(code: str, tags: list[tuple], source: str) -> str:
    tags_text = "\n".join(f"- **{t}**: {d}" for t, d in tags)
    return f"""Você é especialista em SQA aplicado ao LibreOffice (FATEC Cotia 2026).

Analise o código de `{source}` segundo estas dimensões:

{tags_text}

```
{code}
```

Para cada dimensão:
- **Achados**: problemas concretos no código
- **Recomendações**: ações mensuráveis

Finalize com:
**Plano de SQA** — 3 prioridades críticas
**KPIs propostos** — métricas para este módulo"""


@st.cache_data(show_spinner=False)
def load_default_code() -> str:
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/LibreOffice/core/master/sw/source/filter/ww8/wrtw8nds.cxx",
            timeout=10,
        )
        if r.status_code == 200:
            return "\n".join(r.text.splitlines()[:150])
    except Exception:
        pass
    return ""


# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2 = st.tabs(["📂 Análise de Projeto", "🧪 Análise de Código"])


# ── TAB 1: Análise de Projeto ─────────────────────────────────────────────────
with tab1:
    st.markdown("### Importar projeto")

    source = st.radio("Fonte do projeto", ["🔗 Repositório GitHub/GitLab", "📦 Upload ZIP"], horizontal=True, label_visibility="collapsed")
    st.write("")

    if source == "🔗 Repositório GitHub/GitLab":
        url_col, btn_col = st.columns([5, 1])
        with url_col:
            repo_url = st.text_input(
                "URL",
                placeholder="https://github.com/LibreOffice/core/blob/master/sw/source/filter/ww8/wrtw8nds.cxx",
                label_visibility="collapsed",
            )
        with btn_col:
            load_btn = st.button("Carregar", type="primary", use_container_width=True, key="btn_load")

        if load_btn and repo_url:
            is_file = "/blob/" in repo_url or any(repo_url.endswith(e) for e in CODE_EXTS)
            if is_file:
                try:
                    with st.spinner("Buscando arquivo..."):
                        content = fetch_raw(repo_url)
                    fname = repo_url.split("/")[-1]
                    st.session_state.update({"proj_files": {fname: content}, "proj_source": fname})
                    st.session_state.pop("proj_file_list", None)
                    st.session_state.pop("proj_meta", None)
                except Exception as e:
                    st.error(f"Erro ao buscar arquivo: {e}")
            else:
                with st.spinner("Listando arquivos do repositório..."):
                    files, meta = github_file_list(repo_url)
                if files:
                    st.session_state.update({"proj_file_list": files, "proj_meta": meta})
                    st.session_state.pop("proj_files", None)
                    st.success(f"{len(files)} arquivos encontrados.")
                else:
                    st.error(f"Não foi possível listar os arquivos. Meta retornado: `{meta}`. Verifique se a URL é válida ou se o GitHub API não está sendo limitado (60 req/h sem token).")

        if "proj_file_list" in st.session_state and "proj_files" not in st.session_state:
            sel = st.multiselect(
                "Selecione os arquivos para analisar (até 5):",
                st.session_state["proj_file_list"],
                max_selections=5,
            )
            if sel and st.button("Carregar selecionados", type="primary", key="btn_load_sel"):
                meta = st.session_state.get("proj_meta", {})
                u, r, b = meta.get("user"), meta.get("repo"), meta.get("branch", "master")
                loaded = {}
                errors = []
                with st.spinner(f"Carregando {len(sel)} arquivo(s)..."):
                    for path in sel:
                        try:
                            content = fetch_raw(f"https://github.com/{u}/{r}/blob/{b}/{path}")
                            loaded[path] = content
                        except Exception as e:
                            errors.append(f"{path}: {e}")
                if loaded:
                    st.session_state.update({"proj_files": loaded, "proj_source": f"{len(loaded)} arquivo(s)"})
                if errors:
                    st.warning("Alguns arquivos falharam: " + "; ".join(errors))

    else:
        uploaded = st.file_uploader("Arraste o ZIP aqui ou clique para selecionar", type="zip", label_visibility="collapsed")
        if uploaded:
            with st.spinner("Extraindo arquivos..."):
                extracted = files_from_zip(uploaded)
            if extracted:
                st.session_state.update({"proj_files": extracted, "proj_source": uploaded.name})
                st.success(f"{len(extracted)} arquivos de código encontrados.")
            else:
                st.error("Nenhum arquivo de código encontrado no ZIP.")

    # ── Configurar análise ────────────────────────────────────────────────────
    if "proj_files" in st.session_state:
        st.divider()
        proj_files = st.session_state["proj_files"]

        col_info, col_clear = st.columns([5, 1])
        with col_info:
            total_lines = sum(len(v.splitlines()) for v in proj_files.values())
            st.caption(f"{len(proj_files)} arquivo(s) carregado(s) · {total_lines} linhas no total")
        with col_clear:
            if st.button("Limpar", use_container_width=True, key="btn_clear"):
                for k in ["proj_files", "proj_source", "proj_file_list", "proj_meta"]:
                    st.session_state.pop(k, None)
                st.rerun()

        with st.expander(f"Visualizar arquivos ({len(proj_files)})"):
            for fname, code in proj_files.items():
                st.markdown(f"**`{fname}`** — {len(code.splitlines())} linhas")
                st.code(code[:1000] + ("\n..." if len(code) > 1000 else ""), language="cpp")

        # Concatena todos para análise (limitado a 200 linhas por arquivo)
        combined = "\n\n".join(
            f"// ── {fname} ──\n" + "\n".join(code.splitlines()[:200])
            for fname, code in proj_files.items()
        )
        file_key = ", ".join(proj_files.keys())

        st.markdown("**Etapas do framework a analisar:**")
        cols = st.columns(3)
        selected = []
        for i, (tag, desc) in enumerate(ANALYSIS_TAGS):
            with cols[i % 3]:
                if st.checkbox(tag, value=(i in [4, 5]), help=desc, key=f"ptag_{i}"):
                    selected.append((tag, desc))

        st.write("")
        if st.button("▶ Analisar com IA", type="primary", key="btn_analyze"):
            if not selected:
                st.warning("Selecione ao menos uma etapa.")
            else:
                st.divider()
                with st.spinner(f"Analisando {len(proj_files)} arquivo(s)..."):
                    stream_response(build_prompt(combined[:8000], selected, file_key))


# ── TAB 2: Análise de Código ──────────────────────────────────────────────────
with tab2:
    st.markdown("### Analisar trecho de código")

    with st.spinner("Carregando código do LibreOffice Writer..."):
        default = load_default_code()

    st.caption("Código padrão: `sw/source/filter/ww8/wrtw8nds.cxx` — LibreOffice Writer (GitHub)")
    code_input = st.text_area("Código:", value=default, height=280, label_visibility="collapsed")

    lang = st.selectbox("Linguagem:", ["C++", "Python", "Java", "Outro"])

    st.markdown("**Etapas do framework a analisar:**")
    cols2 = st.columns(3)
    selected2 = []
    for i, (tag, desc) in enumerate(ANALYSIS_TAGS):
        with cols2[i % 3]:
            if st.checkbox(tag, value=(i in [4, 5]), help=desc, key=f"ctag_{i}"):
                selected2.append((tag, desc))

    st.write("")
    if st.button("▶ Analisar", type="primary", key="btn_analyze_code"):
        if not code_input.strip():
            st.warning("Cole um código para analisar.")
        elif not selected2:
            st.warning("Selecione ao menos uma etapa.")
        else:
            st.divider()
            with st.spinner("Analisando..."):
                stream_response(build_prompt(code_input[:6000], selected2, f"trecho {lang}"))
