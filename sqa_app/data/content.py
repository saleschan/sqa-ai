"""
Conteúdo estruturado extraído do Relatório Tecnológico.
Fonte: Barboza et al., FATEC Cotia, 2026.
"""

# ── 11 Etapas do Framework ────────────────────────────────────────────────────
STAGES = [
    {
        "num": 1,
        "title": "Planejamento e Definição de Objetivos",
        "description": (
            "Definição de critérios mensuráveis de qualidade a partir da análise de dados históricos "
            "do Bugzilla e relatórios de releases. Geração de KPIs formais validados pela IA Claude."
        ),
        "entrada": "Dados históricos do Bugzilla e relatórios de releases anteriores",
        "atividades": [
            {
                "title": "Definição de critérios mensuráveis",
                "desc": "Estabelecer indicadores formais de qualidade com base em dados históricos do projeto.",
            },
            {
                "title": "Geração de KPIs com IA",
                "desc": "Utilizar a IA Claude para propor e refinar KPIs alinhados ao ciclo de desenvolvimento do LibreOffice.",
            },
            {
                "title": "Validação dos indicadores",
                "desc": "Revisar e validar os KPIs gerados contra requisitos do projeto e benchmarks de projetos open-source similares.",
            },
        ],
        "saida": "Plano de SQA inicial e KPIs formais validados",
        "tools": "IA Claude, Bugzilla, GitLab TDF",
        "owner": "Felipe Sales da Silva",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 2,
        "title": "Coleta e Análise de Requisitos",
        "description": (
            "Análise semântica dos requisitos funcionais e não funcionais do LibreOffice. "
            "Identificação de ambiguidades: requisitos de compatibilidade .docx incompletos, "
            "ausência de acessibilidade WCAG 2.1, falta de especificações para documentos >500 páginas."
        ),
        "entrada": "Documentação pública do LibreOffice e especificações do projeto TDF",
        "atividades": [
            {
                "title": "Análise semântica de requisitos",
                "desc": "Aplicar IA para identificar ambiguidades, conflitos e lacunas nos requisitos funcionais e não funcionais.",
            },
            {
                "title": "Mapeamento de lacunas",
                "desc": "Catalogar requisitos ausentes: compatibilidade .docx incompleta, WCAG 2.1, documentos grandes (>500 págs.).",
            },
            {
                "title": "Priorização de requisitos críticos",
                "desc": "Classificar requisitos por impacto no usuário e viabilidade de implementação.",
            },
        ],
        "saida": "Lista de requisitos inconsistentes e relatório de lacunas identificadas",
        "tools": "IA Claude, documentação pública TDF",
        "owner": "Felipe Sales da Silva",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 3,
        "title": "Projeto e Arquitetura",
        "description": (
            "Mapeamento de hot spots de complexidade. Alto acoplamento entre Writer e o core "
            "identificado como principal impedimento para testes isolados. Priorização da "
            "refatoração do módulo writerfilter/ como intervenção de maior custo-benefício."
        ),
        "entrada": "Código-fonte do repositório GitLab TDF",
        "atividades": [
            {
                "title": "Mapeamento de hot spots de complexidade",
                "desc": "Identificar módulos com alta complexidade ciclomática e acoplamento excessivo usando IA.",
            },
            {
                "title": "Análise de acoplamento",
                "desc": "Avaliar dependências entre Writer e o core que impedem testes isolados.",
            },
            {
                "title": "Priorização de refatorações",
                "desc": "Recomendar intervenções ordenadas por custo-benefício, com foco em writerfilter/.",
            },
        ],
        "saida": "Relatório arquitetural e mapa de complexidade com recomendações de refatoração",
        "tools": "IA Claude, repositório GitLab TDF",
        "owner": "Diego Barboza Pereira",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 4,
        "title": "Desenvolvimento",
        "description": (
            "Revisão de práticas de codificação: ausência de análise estática obrigatória antes "
            "de submissão de patches, uso inconsistente de smart pointers vs ponteiros brutos, "
            "gargalos no code review. Recomendação de integração do CodeClimate e AddressSanitizer."
        ),
        "entrada": "Código-fonte, patches submetidos e diretrizes de contribuição do projeto",
        "atividades": [
            {
                "title": "Revisão de padrões de codificação",
                "desc": "Avaliar uso inconsistente de smart pointers vs ponteiros brutos e identificar padrões inseguros.",
            },
            {
                "title": "Análise estática com IA",
                "desc": "Propor integração obrigatória do CodeClimate e AddressSanitizer ao fluxo de Merge Requests.",
            },
            {
                "title": "Diagnóstico de gargalos no code review",
                "desc": "Identificar pontos de lentidão no processo de revisão e sugerir automações.",
            },
        ],
        "saida": "Diretrizes de codificação atualizadas e lista de melhorias técnicas priorizadas",
        "tools": "IA Claude, CodeClimate, AddressSanitizer",
        "owner": "Diego Barboza Pereira",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 5,
        "title": "Testes e Verificação",
        "description": (
            "Análise da estrutura de testes (CppUnit, Python/UNO, arquivos OOXML). "
            "Cobertura unitária abaixo de 40% em módulos críticos. Proposta de geração automática "
            "de casos de teste por IA, mutation testing assistido e fuzzing contínuo."
        ),
        "entrada": "Código fonte",
        "atividades": [
            {
                "title": "Testes Automatizados Inteligentes",
                "desc": "Desenvolver testes automatizados com IA para cobrir testes unitários, de integração, de sistema e de regressão.",
            },
            {
                "title": "Testes Manuais Assistidos por IA",
                "desc": "Utilizar IA para sugerir casos de teste e verificar resultados de testes manuais.",
            },
            {
                "title": "Testes de Desempenho e Segurança",
                "desc": "Implementar ferramentas de IA para testes de desempenho e segurança.",
            },
        ],
        "saida": "Plano de SQA, Indicadores de desempenho (KPIs)",
        "tools": "IA Claude, CppUnit, Python/UNO, fuzzing",
        "owner": "Giovanni Dos Santos Jeronymo",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 6,
        "title": "Integração Contínua e Entrega Contínua (CI/CD)",
        "description": (
            "Diagnóstico: build time >90 minutos no Jenkins, ausência de build incremental inteligente. "
            "Proposta de análise de impacto por commit, triagem automática de falhas com NLP "
            "e agentes de monitoramento proativo."
        ),
        "entrada": "Código testado",
        "atividades": [
            {
                "title": "Pipeline de CI/CD Inteligente",
                "desc": "Configurar pipelines de CI/CD que utilizem IA para automação do build, testes e implantação.",
            },
            {
                "title": "Monitoramento Proativo de Builds",
                "desc": "Ferramentas de IA para monitorar builds e detectar falhas proativamente.",
            },
        ],
        "saida": "Builds automatizados, Relatórios de monitoramento",
        "tools": "IA Claude, Jenkins, NLP",
        "owner": "Giovanni Dos Santos Jeronymo",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 7,
        "title": "Gerenciamento de Defeitos",
        "description": (
            "Identificação de oportunidades no Bugzilla: classificação automática por NLP, "
            "detecção de duplicatas por similaridade semântica (estimativa 15-20% do total) "
            "e correlação automática bugs/commits via Git blame."
        ),
        "entrada": "Base de dados do Bugzilla e histórico de commits do GitLab TDF",
        "atividades": [
            {
                "title": "Classificação automática por NLP",
                "desc": "Treinar modelo NLP no histórico do Bugzilla para classificar severidade e componente automaticamente.",
            },
            {
                "title": "Detecção de duplicatas por similaridade semântica",
                "desc": "Identificar bugs duplicados antes da submissão, reduzindo a taxa estimada de 15–20%.",
            },
            {
                "title": "Correlação automática bugs/commits",
                "desc": "Cruzar relatórios de bugs com commits via Git blame para agilizar o diagnóstico.",
            },
        ],
        "saida": "Relatório de triagem automatizada e mapa de correlação bugs/commits",
        "tools": "IA Claude, Bugzilla, NLP, Git",
        "owner": "Vitor Hugo Messias",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 8,
        "title": "Feedback e Melhoria Contínua",
        "description": (
            "Análise de feedback em fóruns públicos (Ask LibreOffice, Reddit, Stack Overflow). "
            "Proposta de dashboard consolidado cruzando telemetria opt-in, Bugzilla e redes sociais, "
            "com retrospectivas orientadas por métricas comparativas entre releases."
        ),
        "entrada": "Feedback de usuários em fóruns públicos e dados de telemetria opt-in",
        "atividades": [
            {
                "title": "Análise de feedback por NLP",
                "desc": "Processar automaticamente comentários de fóruns (Ask LibreOffice, Reddit, Stack Overflow) para extrair temas recorrentes.",
            },
            {
                "title": "Dashboard consolidado de feedback",
                "desc": "Cruzar telemetria opt-in, Bugzilla e redes sociais em um painel unificado.",
            },
            {
                "title": "Retrospectivas orientadas por métricas",
                "desc": "Gerar relatórios comparativos entre releases para orientar ciclos de melhoria contínua.",
            },
        ],
        "saida": "Dashboard de feedback consolidado e relatório de retrospectiva por release",
        "tools": "IA Claude, NLP, Telemetria",
        "owner": "Vitor Hugo Messias",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 9,
        "title": "Documentação e Treinamento",
        "description": (
            "Inconsistências identificadas: exemplos desatualizados na API UNO, guia de contribuição "
            "fragmentado, ausência de Doxygen em código legado. Proposta de geração de documentação "
            "por LLM e chatbot de onboarding para novos contribuidores."
        ),
        "entrada": "Código-fonte legado e documentação existente do projeto",
        "atividades": [
            {
                "title": "Identificação de inconsistências na documentação",
                "desc": "Mapear exemplos desatualizados na API UNO, guia de contribuição fragmentado e ausência de Doxygen.",
            },
            {
                "title": "Geração automática de documentação por LLM",
                "desc": "Utilizar LLM para gerar comentários Doxygen em funções complexas do código legado.",
            },
            {
                "title": "Chatbot de onboarding",
                "desc": "Desenvolver assistente conversacional para orientar novos contribuidores da comunidade LibreOffice.",
            },
        ],
        "saida": "Documentação técnica atualizada e chatbot de onboarding operacional",
        "tools": "IA Claude, Doxygen, LLM, Chatbot",
        "owner": "Igor Gabriel Silva Dos Santos",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 10,
        "title": "Governança e Auditoria",
        "description": (
            "Riscos de conformidade: ausência de verificação de licenças (MPLv2/LGPLv3), auditorias "
            "de segurança pontuais e não conformidade com WCAG 2.1. Proposta de integração do FOSSA, "
            "Grype, Semgrep e auditoria de acessibilidade mensal automatizada."
        ),
        "entrada": "Dependências do projeto e código-fonte",
        "atividades": [
            {
                "title": "Verificação contínua de licenças",
                "desc": "Integrar FOSSA ao pipeline para validar conformidade com MPLv2/LGPLv3 em todas as dependências.",
            },
            {
                "title": "Auditoria de segurança automatizada",
                "desc": "Executar Grype e Semgrep em cada Merge Request para detectar vulnerabilidades antes do merge.",
            },
            {
                "title": "Auditoria de acessibilidade",
                "desc": "Implementar verificação mensal automatizada de conformidade com WCAG 2.1.",
            },
        ],
        "saida": "Relatório de conformidade de licenças, auditoria de segurança e acessibilidade",
        "tools": "IA Claude, FOSSA, Grype, Semgrep",
        "owner": "Igor Gabriel Silva Dos Santos",
        "period": "Fev – Mai/2026",
    },
    {
        "num": 11,
        "title": "Lançamento e Manutenção",
        "description": (
            "Principal fragilidade: ausência de monitoramento automatizado de crash reports pós-release. "
            "Proposta de coleta opt-in de telemetria com análise por IA nas primeiras 48h, sistema de "
            "predição de impacto de bugs e painel de saúde pós-lançamento."
        ),
        "entrada": "Release candidata e dados de telemetria opt-in",
        "atividades": [
            {
                "title": "Monitoramento de crash reports pós-release",
                "desc": "Coletar crash reports opt-in e analisar automaticamente com IA nas primeiras 48h após cada release.",
            },
            {
                "title": "Predição de impacto de bugs",
                "desc": "Usar ML para priorizar bugs detectados pós-release com base no impacto estimado ao usuário.",
            },
            {
                "title": "Painel de saúde pós-lançamento",
                "desc": "Dashboard em tempo real cruzando telemetria, crash reports e satisfação do usuário.",
            },
        ],
        "saida": "Relatório pós-lançamento e painel de saúde da release",
        "tools": "IA Claude, Telemetria, ML, Dashboard",
        "owner": "Roger Mendes Coelho",
        "period": "Fev – Mai/2026",
    },
]

# ── Problemas Estruturais ─────────────────────────────────────────────────────
PROBLEMS = [
    {
        "category": "Governança de qualidade",
        "count": 4,
        "detail": (
            "Sem plano formal de SQA. KPIs não rastreáveis. Critérios de qualidade "
            "estabelecidos informalmente em listas de e-mail sem indicadores mensuráveis."
        ),
    },
    {
        "category": "Requisitos e Arquitetura",
        "count": 6,
        "detail": (
            "Requisitos de compatibilidade .docx incompletos. Alto acoplamento entre Writer "
            "e core. Complexidade ciclomática >50 em writerfilter/. Falta de requisitos WCAG 2.1."
        ),
    },
    {
        "category": "Desenvolvimento e Testes",
        "count": 8,
        "detail": (
            "Cobertura de testes <40% em módulos críticos. Ausência de análise estática obrigatória. "
            "Uso inconsistente de smart pointers. Fuzzing não contínuo no pipeline principal."
        ),
    },
    {
        "category": "CI/CD e Gestão de Defeitos",
        "count": 6,
        "detail": (
            "Build time >90 min no Jenkins. Triagem de bugs totalmente manual: atraso médio "
            "2-3 semanas. Taxa de duplicatas 15-20%. >100.000 bugs históricos no Bugzilla."
        ),
    },
    {
        "category": "Documentação e Manutenção",
        "count": 4,
        "detail": (
            "API UNO com exemplos desatualizados. Documentação inline (Doxygen) ausente em código "
            "legado. Nenhum mecanismo automatizado de coleta de crash reports pós-release."
        ),
    },
]

# ── KPIs Formais ──────────────────────────────────────────────────────────────
KPIS = [
    "Taxa de crashes < 2 por mil sessões",
    "Fidelidade de conversão de documentos > 95%",
    "Abertura de arquivos 50 MB em < 8 segundos",
    "Cobertura de testes > 75% em módulos críticos",
    "Menos de 10 bugs de alta prioridade abertos simultaneamente",
]

# ── Principais Recomendações ──────────────────────────────────────────────────
RECOMMENDATIONS = [
    {
        "title": "Triagem automática de bugs por NLP",
        "detail": (
            "Classificação automática de severidade e componente via NLP treinado no histórico do "
            "Bugzilla. Estimativa: redução do atraso de triagem de 3 semanas para menos de 24 horas."
        ),
    },
    {
        "title": "Geração automática de casos de teste por IA",
        "detail": (
            "Mutation testing assistido e integração de fuzzing contínuo com priorização por histórico "
            "de cobertura. Projeção: aumento da cobertura de 40% para mais de 70%."
        ),
    },
    {
        "title": "Monitoramento de crash reports pós-release",
        "detail": (
            "Coleta opt-in de telemetria com análise por IA nas primeiras 48h após cada release. "
            "Redução estimada de 60% no tempo de detecção de regressões críticas."
        ),
    },
    {
        "title": "Detecção de duplicatas por similaridade semântica",
        "detail": (
            "Detecção de bugs duplicados antes da submissão. Pode reduzir a taxa de 15-20% "
            "de duplicatas e liberar voluntários para triagem de issues genuinamente novos."
        ),
    },
    {
        "title": "Análise estática obrigatória no pipeline",
        "detail": (
            "Integração de CodeClimate e AddressSanitizer ao fluxo de Merge Requests. "
            "Detecção automática de uso inseguro de memória antes do merge."
        ),
    },
    {
        "title": "Geração automática de documentação por LLM",
        "detail": (
            "Geração de comentários Doxygen para funções complexas do código legado e "
            "chatbot de onboarding para novos contribuidores da comunidade."
        ),
    },
    {
        "title": "Auditoria contínua de licenças e segurança",
        "detail": (
            "Integração de FOSSA (licenças), Grype e Semgrep (vulnerabilidades) ao pipeline. "
            "Auditoria de acessibilidade WCAG 2.1 mensal automatizada."
        ),
    },
]

# ── Equipe ────────────────────────────────────────────────────────────────────
TEAM = [
    {
        "name": "Diego Barboza Pereira",
        "stages": "3 e 4",
        "role": "Análise arquitetural e revisão de práticas de codificação",
    },
    {
        "name": "Felipe Sales da Silva",
        "stages": "1 e 2",
        "role": "Planejamento, KPIs e análise de requisitos",
    },
    {
        "name": "Giovanni Dos Santos Jeronymo",
        "stages": "5 e 6",
        "role": "Estratégia de testes e diagnóstico de CI/CD",
    },
    {
        "name": "Igor Gabriel Silva Dos Santos",
        "stages": "9 e 10",
        "role": "Documentação e governança/auditoria",
    },
    {
        "name": "Roger Mendes Coelho",
        "stages": "11 e 12",
        "role": "Lançamento, manutenção e consolidação do relatório",
    },
    {
        "name": "Vitor Hugo Messias",
        "stages": "7 e 8",
        "role": "Gerenciamento de defeitos e feedback contínuo",
    },
]

# ── Síntese dos Resultados ────────────────────────────────────────────────────
RESULTS = {
    "inconsistencias": 28,
    "recomendacoes": 32,
    "etapas": 11,
    "usuarios_impactados": "200M+",
    "reducao_triagem": "3 sem → <24h",
    "aumento_cobertura": "40% → 70%+",
    "reducao_deteccao_regressoes": "−60%",
}
