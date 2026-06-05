# 🔬 SQA Tool – LibreOffice × IA

Ferramenta interativa de **Garantia de Qualidade de Software (SQA)** desenvolvida com **Python + Streamlit**, que analisa código-fonte real via IA (LLaMA 3.3 70B via Groq) segundo as 11 etapas do framework proposto no Projeto Integrador IV — FATEC Cotia (2026).

---

## ✨ Funcionalidades

| Aba | Descrição |
|-----|-----------|
| 📂 Análise de Projeto | Importa arquivos de um repositório GitHub/GitLab ou via upload ZIP e analisa múltiplos arquivos de código com IA |
| 🧪 Análise de Código | Cola ou carrega um trecho de código (padrão: `wrtw8nds.cxx` do LibreOffice Writer) para análise imediata |

A IA analisa o código segundo as dimensões do framework:

1. Planejamento — KPIs e plano de SQA  
2. Requisitos — Ambiguidades e lacunas  
3. Arquitetura — Acoplamento e complexidade  
4. Desenvolvimento — Padrões inseguros e análise estática  
5. Testes — Cobertura, regressão e fuzzing  
6. CI/CD — Pipeline, build e monitoramento  
7. Defeitos — Triagem e duplicatas  
8. Feedback — Usabilidade e UX  
9. Documentação — Doxygen e onboarding  
10. Governança — Licenças, segurança e WCAG 2.1  
11. Lançamento — Crash reports e telemetria  

---

## 📁 Estrutura do projeto

```
sqa_app/
├── app.py              # Aplicação principal Streamlit
├── requirements.txt    # Dependências
└── data/
    ├── __init__.py
    └── content.py      # Dados estruturados do relatório (etapas, KPIs, equipe)
```

---

## 🚀 Como executar

### 1. Instalar dependências

```bash
pip install -r sqa_app/requirements.txt
```

### 2. Obter uma API Key gratuita do Groq

Acesse [console.groq.com](https://console.groq.com) e gere uma chave (`gsk_...`).

### 3. Rodar a aplicação

```bash
streamlit run sqa_app/app.py
```

A aplicação abrirá em `http://localhost:8501`. Na tela inicial, informe sua **Groq API Key** para liberar o acesso.

---

## 🔑 Autenticação

A chave é armazenada apenas na sessão do navegador (via `st.session_state`) — não é salva em disco nem enviada para nenhum servidor além da API do Groq.

---

## 🛠️ Stack

| Componente | Tecnologia |
|------------|-----------|
| Interface | Streamlit |
| Modelo IA | LLaMA 3.3 70B Versatile (Groq) |
| Repositórios | GitHub API + GitLab raw |
| Linguagens suportadas | C++, Python, Java, C#, TypeScript, JavaScript |

---

## 👥 Equipe

| Integrante | Etapas | Responsabilidade |
|-----------|--------|-----------------|
| Diego Barboza Pereira | 3 e 4 | Análise arquitetural e revisão de codificação |
| Felipe Sales da Silva | 1 e 2 | Planejamento, KPIs e análise de requisitos |
| Giovanni Dos Santos Jeronymo | 5 e 6 | Estratégia de testes e CI/CD |
| Igor Gabriel Silva Dos Santos | 9 e 10 | Documentação e governança |
| Roger Mendes Coelho | 11 | Lançamento e manutenção |
| Vitor Hugo Messias | 7 e 8 | Gerenciamento de defeitos e feedback |

**Orientadora:** Prof.ª Iza Melão · FATEC Cotia · 2026
