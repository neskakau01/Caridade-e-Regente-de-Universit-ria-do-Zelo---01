import streamlit as st
import time
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal de Acesso Integrado", page_icon="🏢", layout="wide")

# 2. CONTROLE DE ACESSO (Três estados: 'fachada_inicial', 'cruz_negra' ou 'intranet_falsa')
if 'status_login' not in st.session_state:
    st.session_state['status_login'] = 'fachada_inicial'

# Funções para checar as imagens com extensão dupla .jpeg.jpeg
def carregar_logo_fachada():
    possiveis_nomes = ["logo_fachada.jpeg.jpeg", "logo_fachada.png.jpeg", "logo_fachada.jpeg", "logo_fachada.png"]
    for nome in possiveis_nomes:
        if os.path.exists(nome):
            return nome
    return None

def carregar_logo_real():
    possiveis_nomes = ["logo_cruz_negra.jpeg.jpeg", "logo_cruz_negra.png.jpeg", "logo_cruz_negra.jpeg", "logo_cruz_negra.png"]
    for nome in possiveis_nomes:
        if os.path.exists(nome):
            return nome
    return None

# ==============================================================================
# FASE 1: TELA DE FACHADA INICIAL (PORTAL PÚBLICO + TELA DE LOGIN CORPORATIVA)
# ==============================================================================
if st.session_state['status_login'] == 'fachada_inicial':
    st.markdown("""
        <style>
        .stApp { background-color: #f8fafc; color: #1e293b; }
        h1, h2, h3 { color: #0f172a !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        p, li { color: #334155 !important; font-size: 14px; line-height: 1.6; }
        label { color: #1e293b !important; font-weight: 600 !important; }
        
        .card-noticia {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #3b82f6;
            margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .data-noticia { font-size: 11px; color: #64748b; font-weight: bold; }
        
        div.stButton > button:first-child { 
            background-color: #2563eb; 
            color: white; 
            border-radius: 4px; 
            border: none;
            padding: 10px 24px;
            width: 100%;
        }
        div.stButton > button:first-child:hover { background-color: #1d4ed8; color: white; }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #ffffff; padding: 20px; border-bottom: 1px solid #e2e8f0; margin-bottom: 30px; text-align: center;'>
            <h1 style='margin:0; font-size: 24px;'>🏢 Caridade e Regente Universitária do Zelo</h1>
            <p style='margin:5px 0 0 0; color: #64748b !important;'>Portal de Transparência, Alocação de Recursos e Intranet de Colaboradores</p>
        </div>
        """, unsafe_allow_html=True)

    col_esquerda, col_centro, col_direita = st.columns([1.2, 1, 1.2], gap="large")
    
    with col_esquerda:
        st.subheader("Nossa Atuação Institucional")
        st.write("""
        A **Caridade e Regente Universitária do Zelo** opera como uma comunidade integrada de suporte acadêmico, especializada na coleta, logística e distribuição de insumos e infraestrutura de alta complexidade para instituições de ensino superior.
        """)
        
        st.markdown("""
        <div class="card-noticia" style="border-left-color: #10b981;">
            <h4 style='margin:0 0 5px 0; font-size:14px; font-weight:bold;'>Suporte a Ciências Médicas</h4>
            <p style='margin:0; font-size:13px;'>Gerenciamento e fornecimento de materiais biológicos e anatômicos essenciais para o avanço dos laboratórios de anatomia e patologia em faculdades de medicina credenciadas.</p>
        </div>
        <div class="card-noticia" style="border-left-color: #10b981;">
            <h4 style='margin:0 0 5px 0; font-size:14px; font-weight:bold;'>Infraestrutura e Logística Espacial</h4>
            <p style='margin:0; font-size:13px;'>Cessão e mapeamento de amplas áreas abertas e centers de treinamento para laboratórios e faculdades de Educação Física, garantising espaço técnico seguro para atividades externas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_centro:
        st.markdown("<div style='background-color: #ffffff; padding: 25px; border-radius: 8px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); text-align: center;'>", unsafe_allow_html=True)
        
        caminho_fachada = carregar_logo_fachada()
        if caminho_fachada:
            st.image(caminho_fachada, width=160)
            
        st.markdown("<h3 style='font-size: 18px; margin-top: 15px;'>Área Restrita do Colaborador</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 13px; color: #64748b;'>Autenticação requerida para o banco de dados institucional.</p>", unsafe_allow_html=True)
        
        usuario_input = st.text_input("Usuário:")
        senha_input = st.text_input("Senha:", type="password")
        
        st.write("")
        if st.button("Entrar no Sistema"):
            if usuario_input == "" or senha_input == "":
                st.warning("Por favor, preencha todos os campos de autenticação.")
            # ACESSO REAL (Cruz Negra)
            elif usuario_input == "W" and senha_input == "24\\12k-0Y":
                with st.spinner("Descriptografando chaves de segurança..."):
                    time.sleep(2.5)
                st.session_state['status_login'] = 'cruz_negra'
                st.rerun()
            # ACESSO FALSO (Qualquer outro usuário ou senha joga na Intranet de Fachada)
            else:
                with st.spinner("Conectando ao servidor institucional..."):
                    time.sleep(1.5)
                st.session_state['status_login'] = 'intranet_falsa'
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_direita:
        st.subheader("Nicho Investidor e Gestão de Riscos")
        st.write("""
        Gerenciamos parcialmente os ativos financeiros de nossas empresas parceiras através de um sistema interno de flutuação de mercado, mitigando incidentes operacionais severos.
        """)
        
        st.markdown("""
        <div class="card-noticia">
            <span class="data-noticia font-mono">ÍNDICE DE ATIVOS ATUALIZADO</span>
            <h4 style='margin:5px 0; font-size:14px; font-weight:bold;'>Ajuste de Portfólio: Setor Alimentício (Fábricas de Chocolate)</h4>
            <p style='margin:0; font-size:13px;'>Identificadas anomalias estruturais e operacionais em uma de nossas unidades de manufatura. Iniciado o protocolo padrão de retirada parcial de capital preventivo para contenção de danos e desvalorização estratégica controlada de ativos.</p>
        </div>
        <div class="card-noticia">
            <span class="data-noticia font-mono">DIRETRIZ DE REAQUISIÇÃO</span>
            <h4 style='margin:5px 0; font-size:14px; font-weight:bold;'>Retorno de Investimento Pós-Saneamento</h4>
            <p style='margin:0; font-size:13px;'>Após a intervenção de nossas equipes de auditoria de campo para a resolução dos problemas técnicos locais, o plano de recompra massiva de ações será executado, visando a estabilização e subsequente expansão econômica.</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# FASE 2: INTRANET DE FACHADA (TELA CORPORATIVA FALSA PARA ENGANAR CURIOSOS)
# ==============================================================================
elif st.session_state['status_login'] == 'intranet_falsa':
    st.markdown("""
        <style>
        .stApp { background-color: #f1f5f9; color: #334155; }
        h1, h2, h3 { color: #1e293b !important; font-family: 'Segoe UI', sans-serif; }
        
        /* CORREÇÃO DO TEXTO BRANCO NAS ABAS: força a fonte a ficar escura perto do preto */
        .stTabs [data-baseweb="tab"] p {
            color: #1e293b !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }
        
        .painel-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .painel-box h4, .painel-box h5, .painel-box p, .painel-box li {
            color: #1e293b !important;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Barra lateral corporativa de mentira
    st.sidebar.markdown("<h3 style='text-align:center; color:#2563eb !important;'>Painel do Usuário</h3>", unsafe_allow_html=True)
    caminho_fachada = carregar_logo_fachada()
    if caminho_fachada:
        st.sidebar.image(caminho_fachada, use_container_width=True)
    
    st.sidebar.write("---")
    st.sidebar.write("👤 **Colaborador:** Conectado como Usuário Externo")
    st.sidebar.write("🔑 **Nível de Acesso:** Padrão / Administrativo")
    
    if st.sidebar.button("Encerrar Sessão (Logout)"):
        st.session_state['status_login'] = 'fachada_inicial'
        st.rerun()

    # Cabeçalho da Intranet Falsa
    st.markdown("""
        <div style='background-color: #ffffff; padding: 20px; border-bottom: 2px solid #3b82f6; margin-bottom: 25px; border-radius:4px;'>
            <h2 style='margin:0; font-size: 22px; color: #2563eb !important;'>🏢 Intranet Administrativa - Área de Colaboradores</h2>
            <p style='margin:5px 0 0 0; color: #64748b !important;'>Caridade e Regente Universitária do Zelo — Gestão Logística e Acadêmica</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("📊 **Aviso do Sistema:** Seu terminal de acesso está operando em modo de visualização padrão. Modificações cadastrais exigem assinatura eletrônica da gerência.")
    
    # Abas antigas corrigidas + Novas abas de aprofundamento institucionais
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📋 Controle de Insumos", 
        "📑 Atas de Reuniões", 
        "📈 Gráficos de Repasse",
        "📜 Nossa História",
        "👥 Corpo de Direção",
        "🌱 Sustentabilidade",
        "🤝 Parcerias Sociais"
    ])
    
    with tab1:
        st.markdown("""
        <div class="painel-box">
            <h4>Alocação de Materiais Anatômicos (Ciências Médicas)</h4>
            <p>Listagem de repasses efetuados para os laboratórios credenciados neste trimestre de 2026:</p>
            <ul>
                <li><b>Lote #884-A:</b> Modelos de resina e tecidos de treinamento cirúrgico (Entregue - Campus Central).</li>
                <li><b>Lote #887-B:</b> Peças biológicas conservadas para dissecção patológica (Retido para conferência de notas fiscais).</li>
                <li><b>Lote #890-C:</b> Lâminas histológicas e reagentes de fixação celular (Em trânsito).</li>
            </ul>
        </div>
        <div class="painel-box">
            <h4>Infraestrutura Desportiva (Educação Física)</h4>
            <p>Mapeamento de praças técnicas externas e arenas esportivas de treinamento:</p>
            <ul>
                <li><b>Setor Sul:</b> Liberação de pista de atletismo e quadras poliesportivas para testes de fisiologia do esforço.</li>
                <li><b>Setor Norte (Fluvial):</b> Agendamento de treinos de campo suspensos temporariamente devido a readequações ambientais da prefeitura.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("""
        <div class="painel-box">
            <h5>Ata Ordinária #104 - Conselho Administrativo</h5>
            <p style="font-size:12px; color:#64748b !important;">Data: 14 de Março de 2026 | Presidência de Gestão</p>
            <p><i>"Ficou deliberado por unanimidade que as auditorias financeiras nas subsidiárias de produção de alimentos (Setor de Manufatura de Doces e Derivados) passarão a ser coordenadas por escritórios terceirizados, visando a blindagem patrimonial da mantenedora principal contra as oscilações bruscas verificadas na Bolsa de Valores no último mês..."</i></p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        st.markdown("<div class='painel-box'>", unsafe_allow_html=True)
        st.subheader("Gráfico de Distribuição Orçamentária")
        st.bar_chart({"Insumos Médicos": 45, "Logística de Espaço": 35, "Auditorias de Ativos": 20})
        st.markdown("</div>", unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div class="painel-box">
            <h4>Fundação e Trajetória Institucional</h4>
            <p>Fundada em meados do século passado sob os preceitos de amparo civilizatório e suporte acadêmico, a <b>Caridade e Regente Universitária do Zelo</b> nasceu como uma sociedade filantrópica voltada à unificação de grandes eixos acadêmicos federais e estaduais.</p>
            <p>Originalmente criada para mitigar a escassez de infraestrutura pesada em polos universitários interioranos, a organização expandiu-se rapidamente através de doações de grandes heranças corporativas e fundos de investimentos privados. Hoje, atuamos em regime de cogestão logística, garantindo que os centros de pesquisa operem com estabilidade física, estrutural e financeira mesmo sob crises econômicas severas no mercado nacional.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab5:
        st.markdown("""
        <div class="painel-box">
            <h4>Mesa Regente de Governança</h4>
            <p>A governança das atividades da organização é rigidamente estruturada por membros de notório saber administrativo e fiscal:</p>
            <ul>
                <li><b>Diretor Geral de Patrimônio:</b> Dr. Alencastro Peixoto (Responsável pela custódia de áreas e concessões imobiliárias).</li>
                <li><b>Vice-Diretor Executivo:</b> Prof. Marcus Vinícius Toledo (Coordenador técnico das cadeias de suprimentos e alocação).</li>
                <li><b>Conselheira Consultiva Principal:</b> Dra. Ana Carter (Representante de Ativos Estratégicos).</li>
                <li><b>Ouvidoria e Compliance:</b> Controladoria Interna de São Miguel dos Antares.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab6:
        st.markdown("""
        <div class="painel-box">
            <h4>Contribuições e Gestão Ecológica Vetorial</h4>
            <p>Nossos complexos de treinamento externo e praças desportivas seguem os mais estritos protocolos ecológicos contemporâneos:</p>
            <ul>
                <li><b>Recuperação de Áreas Degradadas:</b> Projetos de reflorestamento controlado de matas ciliares e entornos periféricos em zonas industriais desativadas.</li>
                <li><b>Tratamento de Efluentes Químicos:</b> Monitoramento rigoroso do descarte de reagentes e fixadores laboratoriais em parceria com agências ambientais.</li>
                <li><b>Neutralização de Carbono:</b> Auditorias anuais de frotas logísticas de transporte pesado para garantir o cumprimento das metas internacionais de emissão zero.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab7:
        st.markdown("""
        <div class="painel-box">
            <h4>Expansão de Projetos Sociais Interdisciplinares</h4>
            <p>Além da tradicional alocação direcionada às áreas de Medicina e Educação Física, a instituição mantém ativos de suporte em outros departamentos cruciais:</p>
            <ul>
                <li><b>Faculdades de Agronomia e Engenharia Ambiental:</b> Cessão de fazendas-modelo experimentais para mapeamento de lavouras e testes de solos agrícolas sem riscos fitossanitários.</li>
                <li><b>Faculdades de Pedagogia e Ciências Sociais:</b> Financiamento do programa <i>"Zelo Integrado"</i>, que promove a alfabetização de jovens e adultos em comunidades vizinhas às nossas sedes fabris.</li>
                <li><b>Infraestrutura de Telecomunicações:</b> Cooperação técnica com laboratórios de Engenharia para o desenvolvimento de redes locais de rádio internas e canais de segurança criptografados.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# FASE 2: BANCO DE DADOS REAL - SÉRIO & ULTRA SECRETO
# ==========================================
else:
    st.markdown("""
        <style>
        .stApp { background-color: #0c0c0c; color: #dcdcdc; font-family: 'Courier New', Courier, monospace; }
        .cabecalho-cn {
            background-color: #141414;
            padding: 25px;
            border-left: 8px solid #8b0000;
            border-bottom: 2px solid #222222;
            margin-bottom: 25px;
        }
        .aviso-critico {
            background-color: #240505;
            border: 1px solid #ff0000;
            padding: 15px;
            color: #ff3333;
            font-weight: bold;
            font-size: 12px;
            margin-bottom: 25px;
            letter-spacing: 1px;
            line-height: 1.5;
        }
        .bloco-confidencial {
            background-color: #111111;
            border: 1px solid #333333;
            padding: 20px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
        .bloco-desbloqueado {
            background-color: #0d1f11;
            border: 1px solid #2e7d32;
            padding: 20px;
            border-radius: 4px;
            margin-top: 15px;
            margin-bottom: 20px;
        }
        .tag-vermelha {
            color: #ff3333 !important;
            font-weight: bold;
        }
        .tag-verde {
            color: #4caf50 !important;
            font-weight: bold;
        }
        /* Tarja de censura atualizada para Branco */
        .tarja-censurada {
            background-color: #ffffff;
            color: #ffffff;
            padding: 0 4px;
        }
        
        /* NOVO ESTILO: Crachá de Agente com Fundo Branco */
        .badge-container {
            background-color: #ffffff; /* Fundo Branco puro para contraste */
            border: 2px solid #8b0000; /* Borda Vermelho Escuro Tática */
            border-left: 10px solid #8b0000;
            padding: 25px;
            border-radius: 8px;
            max-width: 550px;
            margin: 20px auto;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            color: #000000 !important; /* Força o texto para Preto */
        }
        
        .badge-label {
            color: #444444 !important; /* Cinza Escuro para os labels */
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace !important;
        }

        .badge-value {
            color: #000000 !important; /* Preto para os valores principais */
            font-weight: bold;
            font-family: 'Courier New', Courier, monospace !important;
        }
        
        .badge-header {
            text-align: center;
            border-bottom: 1px solid #cccccc;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        
        .badge-title-cn {
            color: #8b0000 !important;
            font-weight: bold;
            font-size: 14px;
            letter-spacing: 2px;
            font-family: 'Courier New', Courier, monospace !important;
        }
        
        .badge-subtitle-cn {
            color: #666666 !important;
            font-size: 10px;
            letter-spacing: 1px;
            font-family: 'Courier New', Courier, monospace !important;
        }
        
        .badge-footer {
            margin-top: 20px;
            border-top: 1px dashed #dddddd;
            padding-top: 10px;
            font-size: 9px;
            color: #777777 !important;
            text-align: justify;
            line-height: 1.3;
            font-family: 'Courier New', Courier, monospace !important;
        }
        
        /* Ajuste tático para evitar quebra de ícones nativos */
        h1, h2, h3, h4, p, li {
            color: #c8c8c8 !important;
            font-family: 'Courier New', Courier, monospace !important;
        }
        /* Aplica a fonte apenas dentro dos nossos blocos de dados */
        .bloco-confidencial *, .bloco-desbloqueado * {
            font-family: 'Courier New', Courier, monospace !important;
        }
        div.row-widget.stRadio > div { background-color: #111111; padding: 12px; border: 1px solid #222222; }
        </style>
        """, unsafe_allow_html=True)

    caminho_real = carregar_logo_real()
    if caminho_real:
        st.sidebar.image(caminho_real, use_container_width=True)

    st.markdown("""
        <div class="cabecalho-cn">
            <h1 style='margin:0; color:#990000 !important; font-weight:bold; letter-spacing: 3px;'>CRUZ NEGRA: ASCENSÃO</h1>
            <p style='margin:5px 0 0 0; font-size:11px; color:#666666 !important; letter-spacing: 1px;'>SISTEMA CENTRAL DE INFORMAÇÕES DE SEGURANÇA NACIONAL E OCULTAMENTO VETORIAL</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="aviso-critico">
            PROPRIEDADE DA DIRETORIA GERAL DA FUNDAÇÃO — RESTRITO APENAS A PESSOAL AUTORIZADO.<br>
            A REPRODUÇÃO, TRANSFERÊNCIA OU VISUALIZAÇÃO DESTE TERMINAL POR INDIVÍDUOS SEM DEVIDA PATENTE DE COMPATIBILIDADE PSÍQUICA CONSTITUI CRIME DE ALTA TRAIÇÃO SOB O DECRETO INTERNO MILITAR 0-14. MONITORAMENTO DE RETINA ATIVO.
        </div>
        """, unsafe_allow_html=True)

    st.sidebar.markdown("<p style='color:#aa0000; font-weight:bold; text-align:center; letter-spacing:1px; margin-bottom:5px;'>DIRETÓRIOS CRÍTICOS</p>", unsafe_allow_html=True)
    
    # Menu lateral atualizado com o nome profissional e sem emoji
    opcao = st.sidebar.radio("Selecionar Arquivo:", [
        "Terminal Central / Diretoria",
        "Tratado de Ocultamento Sobrenatural",
        "Hierarquia e Níveis de Liberação",
        "Protocolos de Fé e Resiliência",
        "Relatórios de Expedição de Campo",
        "Especializações de Agentes",
        "Gerador de Credencial Tática",
        "Gerenciador de Ficha Ativa",  # <-- NOVA ABA AQUI
        "Relatório de Falha Sistêmica: Marco 96"
    ])

    # --- DIRETÓRIO 1: TERMINAL CENTRAL ---
    if opcao == "Terminal Central / Diretoria":
        st.subheader("TERMINAL DE COMANDO OPERACIONAL")
        st.write("Conexão estabelecida com o servidor Base-01. Sessão activa sob a identificação da Diretoria.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-desbloqueado" style="border-color: #8b0000; background-color: #160505;">
            <h3 style='color: #ff3333 !important; margin-top:0; font-weight:bold; letter-spacing:1px;'>▲ RECONHECIMENTO DE ACESSO: SINAL CONFIRMADO</h3>
            <p><b>Saudações, Agente.</b> Seu terminal foi criptografado com sucesso através dos nossos canais de supressão de rede. A partir deste momento, suas ações, consultas e históricos estão diretamente vinculados à sua assinatura neural.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="bloco-confidencial">
            <h4 style='color:#aa0000 !important; font-weight:bold; margin-top:0;'>ESTADO DA DIRETORIA</h4>
            <p><b>Autoridade Máxima Ativa:</b> Diretora Ana Carter</p>
            <p><b>Status da Infraestrutura:</b> <span style='color:#00ff00;'>ESTÁVEL</span></p>
            <p><b>Índice de Dissipação de Névoa:</b> Controlado dentro dos parâmetros de segurança da comunidade.</p>
            <br>
            <p><i>"A ignorância civil não é uma falha do nosso sistema, é o nosso maior produto. Mantemos a escuridão contida para que o mundo possa continue caminhando sob a luz de uma falsa normalidade."</i><br>
            — <b>Diretora Ana Carter</b>, Pronunciamento no Conselho Superior.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="bloco-confidencial" style="border-left: 4px solid #ff3333;">
            <h4 style='color:#ff3333 !important; font-weight:bold; margin-top:0; letter-spacing:1px;'>⚠️ CÓDIGO DE CONDUTA E DIRETRIZES RÍGIDAS (DECRETO 0-14)</h4>
            <p>Qualquer agente em posse destas credenciais deve seguir estritamente os três pilares de silenciamento estrutural. O não cumprimento acarretará em rebaixamento biológico imediato:</p>
            <ol>
                <li><b>Vedações de Compartilhamento:</b> É terminantemente proibida a replicação, transcrição ou menção visual das informações contidas neste diretório para civis ou agentes de Patente Inferior (Níveis 1 a 3).</li>
                <li><b>Rastreamento Ativo:</b> Este sistema opera sob varredura contínua de IPs geolocalizados. Caso seja detectada uma tentativa de login externa por indivíduos não catalogados utilizando esta chave, o protocolo de quebra de sigilo será ativado.</li>
                <li><b>A Diretriz de Caça:</b> <i>Invasores, interceptadores ou ex-colaboradores dissidentes que acessarem este portal sem autorização expressa da Diretoria serão ativamente caçados, neutralizados psicologicamente e capturados pelas equipes de elite de Nível 7 (Líderes de Caça). Seus registros civis serão completamente apagados e seus corpos destinados à análise bio-anatomia estrutural de laboratórios parceiros. Não há julgamento. Há saneamento.</i></li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    # --- DIRETÓRIO 2: ORIGEM DA ORGANIZAÇÃO ---
    elif opcao == "Tratado de Ocultamento Sobrenatural":
        st.subheader("ARQUIVO DE DIRETRIZ HISTÓRICA: A FUNDAÇÃO")
        st.write("Compilado de documentos históricos, registros de fundação e incidentes clássicos pré-século XXI.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-confidencial">
            <h4 style='color:#aa0000 !important; font-weight:bold;'>VISÃO GERAL OPERACIONAL</h4>
            <p><b>Designação Sistêmica:</b> Coalizão Paramilitar Cruz Negra</p>
            <p><b>Data de Estabelecimento Territorial:</b> Desconhecida (Registros formais iniciados em 1889)</p>
            <p><b>Diretriz Primária:</b> Localizar, isolar e suprimir manifestações de espectro paranormal e vetores biológicos anômalos que ameacem a estabilidade social civil. A preservação do segredo institucional sobrepõe-se a quaisquer leis ou soberanias nacionais.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>DOCUMENTO REGISTRADO: INCIDENTE-1889-OURO</b></span><br>
            <b>Localização de Origem:</b> Região Central de Minas Gerais (Antigas Minas de Exploração)<br>
            <b>Data do Evento:</b> 14 de Novembro de 1889<br><br>
            <b>Descrição do Caso:</b> Durante uma escavação profunda em veios de mineração desativados, operários relataram a abertura de uma fenda subterrânea de onde emanava uma névoa densa de coloração escura que causava colapso psíquico imediato e manifestações físicas espasmódicas nos trabalhadores.<br><br>
            <b>Intervenção Primordial:</b> Destacamentos precursores da organização (então operando sob a alcunha de <i>Ordem do Selo Escuro</i>) isolaram a boca da mina. Foi utilizado o método de selamento por detonação controlada e contenção química por reagentes à base de chumbo. Trinta e dois mineiros afetados foram retidos permanentemente para análise bio-anatomia estrutural. Nenhuma informação foi vazada para a imprensa imperial da época.
        </div>
        """, unsafe_allow_html=True)

        nome_imagem_1 = "registro_historico_1889.png"
        if os.path.exists(nome_imagem_1):
            st.image(nome_imagem_1, caption="[FOTO ARQUIVADA] Registro fotográfico da equipe de selamento primário no setor de mineração (1889)", width=500)
        else:
            st.info(f"💡 [Espaço de Mídia] Salve a foto deste caso na pasta do código com o nome exato de: {nome_imagem_1}")

        st.write("")

        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>DOCUMENTO REGISTRADO: PROTOCOLO-1974-NÉVOA</b></span><br>
            <b>Localização de Origem:</b> Fronteira de Isolamento Fluvial - Setor Norte<br>
            <b>Data do Evento:</b> 03 de Agosto de 1974<br><br>
            <b>Descrição do Caso:</b> Um posto avançado militar de fronteira civil foi completamente silenciado após a manifestação de um fenômeno atmosférico anômalo classificado como 'Névoa de Supressão Cognitiva'. Patrulhas de reconhecimento enviadas pelo exército regular relataram que a estrutura física do posto permanecia intacta, porém todos os vinte e quatro soldados destacados haviam desaparecido, restando apenas seus uniformes, armamentos intocados e marcas de corrosão espiritual nas paredes.<br><br>
            <b>Ação de Campo:</b> Agentes de Operações Especiais da Cruz Negra interceptaram as patrulhas civis antes do retorno à base principal. Foi aplicado o primeiro teste em larga escala do Composto Amnésico Classe B na região. O posto militar foi riscado dos mapas cartográficos oficiais através de manobras burocráticas no Ministério da Defesa, sendo transformado em uma Zona de Exclusão Permanente sob o disfarce de reserva ecológica restrita.
        </div>
        """, unsafe_allow_html=True)

        nome_imagem_2 = "zona_exclusao_1974.png"
        if os.path.exists(nome_imagem_2):
            st.image(nome_imagem_2, caption="[FOTO ARQUIVADA] Perímetro de isolamento tático e monitoramento de névoa no setor fluvial (1974)", width=500)
        else:
            st.info(f"💡 [Espaço de Mídia] Salve a foto deste caso na pasta do código com o nome exato de: {nome_imagem_2}")

        st.write("")

        st.markdown("""
        <div class="bloco-confidencial">
            <h4 style='color:#aa0000 !important; font-weight:bold;'>FILOSOFIA DE APAGAMENTO VETORIAL</h4>
            <p>A Cruz Negra não busca a compreensão pública ou a aclamação de seus atos. Desde o século XIX, nossa engrenagem opera baseada no tripé:</p>
            <ul>
                <li><b>Contenção Física Imediata:</b> Neutralizar o foco da anomalia antes que a malha da realidade local seja permanentemente afetada.</li>
                <li><b>Saneamento Informativo:</b> Criação de narrativas de fachada (fugas de gás, crises financeiras, acidentes estruturais) através de corporações parceiras ligadas ao Nicho Investidor.</li>
                <li><b>Recrutamento de Resiliência:</b> Absorver indivíduos afetados por incidentes que demonstraram compatibilidade psíquica para atuar na linha de frente, descartando materiais biológicos excedentes de forma segura.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- DIRETÓRIO 3: GRAUS DOS AGENTES ---
    elif opcao == "Hierarquia e Níveis de Liberação":
        st.subheader("DOCUMENTO DE GESTÃO DE PESSOAL: GRAUS DE AGENTES")
        st.write("Abaixo estão listados os níveis de liberação tática e modificação biológica autorizados pela Diretora Ana Carter.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-confidencial">
            <p><b class="tag-vermelha">Nível 1 - AT (Agente em Treinamento):</b> Alocados na triagem e suporte periférico. Não possuem autorização para contato direto com anomalias de Classe Vetorial Ativa sem supervisão.</p>
            <p><b class="tag-vermelha">Nível 2 - AA (Agente Aprendiz):</b> Treinados em protocols básicos de supressão psíquica. Autorizados a participar de perímetros de isolamento secundários.</p>
            <p><b class="tag-vermelha">Nível 3 - AB (Agente Básico):</b> Espinha dorsal tática da organização. Possuem estabilização psicológica comprovada e armamento adaptado para interferência de espectro leve.</p>
            <p><b class="tag-vermelha">Nível 4 - AC (Agente de Campo):</b> Veteranos de combate anômalo. Responsáveis pela liderança de incursões urbanas e aplicação imediata de protocolos de sigilo na comunidade.</p>
            <p><b class="tag-vermelha">Nível 5 - CT (Caçador em Treinamento):</b> Selecionados para o programa avançado de erradicação. Iniciam os testes de exposição direta à energia espiritual purificada.</p>
            <p><b class="tag-vermelha">Nível 6 - CA (Caçador de Área):</b> Destinados à contenção de anomalias territoriais massivas. Possuem autonomia tática para decretar quarentenas econômicas e físicas.</p>
            <p><b class="tag-vermelha">Nível 7 - LC (Líder de Caça):</b> O ápice operacional da Cruz Negra. Agentes modificados com alto grau de resiliência a distorções da realidade, respondendo diretamente à Diretora Ana Carter.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- DIRETÓRIO 4: PROTOCOLOS DE FÉ ---
    elif opcao == "Protocolos de Fé e Resiliência":
        st.subheader("DIRETRIZES DE SEGURANÇA E PROTOCOLOS DE FÉ")
        st.write("Códigos procedimentais obrigatórios para a manutenção da sanidade e eficácia em combate.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-confidencial">
            <h4>Protocolo I — Resiliência Dogmática Inabalável</h4>
            <p>Diante de manifestações espectrais, o agente não deve processar a imagem como um evento maleável. A mente deve se ancorar nos axiomas matemáticos da Base. A dúvida enfraquece a barreira psíquica e permite a transmutação biológica induzida pelo ambiente.</p>
        </div>
        <div class="bloco-confidencial">
            <h4>Protocolo II — Saneamento de Vetores Econômicos</h4>
            <p>Caso uma das propriedades ou empresas controladas pelo Nicho Investidor apresente quebra de barreira física (ex: events de infestação em cadeias produtivas), o protocolo de liquidação deve ser ativado imediatamente. O desinvestimento artificial derruba o valor das ações, justificando o esvaziamento do local antes do envio da equipe de Caça.</p>
        </div>
        <div class="bloco-confidencial">
            <h4>Protocolo III — Contenção de Material Biológico Humano</h4>
            <p>O fornecimento de tecidos orgânicos para laboratórios parceiros sob a fachada de estudos de medicina deve seguir os critérios de eliminação de rastros de energia residual. Nenhum cadáver anômalo pode ser descartado em solo público sem a devida aplicação do reagente de cinzas.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- DIRETÓRIO 5: RELATÓRIOS DE EXPEDIÇÃO ---
    elif opcao == "Relatórios de Expedição de Campo":
        st.subheader("LOGS DE MISSÕES DE CAMPO INTERCEPTADOS [SECRETO]")
        st.write("Registros históricos de incursões táticas autorizadas pela administração central. Requer senha criptográfica para visualização total.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-04A</b></span><br>
            <b>Localização:</b> Setor Industrial Sul - Fábrica de Processamento de Doces [CONFIDENCIAL]<br>
            <b>Status da Missão:</b> Concluída / Sucesso Parcial<br>
            <b>Descrição Básica:</b> Relatada flutuação gravitacional na ala de caldeiras e liquefação orgânica de matéria-prima. Uma equipe infiltrada localizou o foco paranormal. <span class="tarja-censurada">OS AGENTES DETECTARAM QUE A ANOMALIA SE ALIMENTAVA DE</span>. Os funcionários sobreviventes receberam amnésicos de Classe C.
        </div>
        """, unsafe_allow_html=True)
        
        exp_1 = st.expander("🔑 DESCRIPTOGRAFAR ARQUIVO EXP-2026-04A")
        with exp_1:
            senha_log1 = st.text_input("Insira a chave de decodificação tática (Log 1):", type="password", key="pwd_log1")
            if senha_log1 == "37\\18m-4X":
                st.markdown("""
                <div class="bloco-desbloqueado">
                    <span class="tag-verde">✔ ACESSO AUTORIZADO — PATENTE DIRETORIA</span><br><br>
                    <b>RELATÓRIO TÁTICO INTEGRAL:</b><br>
                    <b>Equipe de Incursão:</b> Agente de Campo <i>Sargento Marcos Rocha</i> (AC), Agente de Campo <i>Tenente Cavalcanti</i> (AC) e Agente Básico <i>Rodrigo "Marreta" Silva</i> (AB).<br><br>
                    <b>Entidade Identificada:</b> Vetor-09 ("A Massa Voraz"). Uma massa amorfa de glicose transmutada e tecido biológico fundido que gerava campos de microgravidade localizada.<br><br>
                    <b>Resumo do Confronto:</b> Ao entrarem na zona de caldeiras, a equipe foi atacada por tentáculos de matéria orgânica fervente. O Agente <i>Rodrigo</i> foi suspenso no ar pela anomalia gravitacional e arremessado contra a estrutura metálica secundária.<br><br>
                    <b>Desfecho:</b> O núcleo da Entidade foi destruído utilizando cargas de fragmentação térmica purificada. O espécime foi totalmente <b>ELIMINADO</b> no local, impossibilitando a captura de amostras limpas.<br><br>
                    <b>Baixas/Danos:</b> <span class="tag-vermelha"><b>ÓBITO CONFIRMADO</b></span> do Agente <i>Rodrigo Silva</i> (traumatismo craniano severo e exposição térmica). Corpo incinerado no local seguindo o Protocolo III. Os agentes <i>Rocha</i> e <i>Cavalcanti</i> sofreram queimaduras leves, mas permanecem ativos.
                </div>
                """, unsafe_allow_html=True)
            elif senha_log1:
                st.error("Chave incorreta. Tentativa de violação registrada no Terminal Central.")

        st.write("")

        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-05D</b></span><br>
            <b>Localização:</b> Campus Universitário [CONFIDENCIAL] - Ala de Anatomia Médica<br>
            <b>Status da Missão:</b> Arquivada / Contida<br>
            <b>Descrição Básica:</b> Um dos corpos fornecidos apresentou atividade muscular pós-morte espontânea e vocalização em frequências prejudiciais. Agentes do Grau AB agiram redirecionando estudantes. <span class="tarja-censurada">O CADÁVER MANIFESTOU EXPANSÃO DE</span>. O espécime foi tratado conforme o Protocolo III.
        </div>
        """, unsafe_allow_html=True)
        
        exp_2 = st.expander("🔑 DESCRIPTOGRAFAR ARQUIVO EXP-2026-05D")
        with exp_2:
            senha_log2 = st.text_input("Insira a chave de decodificação tática (Log 2):", type="password", key="pwd_log2")
            if senha_log2 == "37\\18m-4X":
                st.markdown("""
                <div class="bloco-desbloqueado">
                    <span class="tag-verde">✔ ACESSO AUTORIZADO — PATENTE DIRETORIA</span><br><br>
                    <b>RELATÓRIO TÁTICO INTEGRAL:</b><br>
                    <b>Equipe de Incursão:</b> Agente Básico <i>Sandro Costa</i> (AB), Agente Básico <i>Felipe Azevedo</i> (AB) e Caçador em Treinamento <i>Guilherme "Farol" Souza</i> (CT).<br><br>
                    <b>Entidade Identificada:</b> Sujeito Necrótico-04. Um cadáver humano modificado por resíduos de névoa de espectro inferior, capaz de projetar ondas sonoras que colapsavam o sistema nervoso periférico de alvos vivos.<br><br>
                    <b>Resumo do Confronto:</b> A criatura ergueu-se da mesa de dissecção durante a madrugada. A equipe bloqueou as saídas acústicas da ala de medicina. O espécime tentou uma ruptura perfurando a parede de drywall utilizando garras ósseas recém-projetadas.<br><br>
                    <b>Desfecho:</b> O Caçador <i>Guilherme</i> utilizou o Protocolo de Fé I para estabilizar a barreira psíquica da equipe e conter os ataques sonoros. A criatura foi imobilizada com correntes de contenção estática e posteriormente <b>CAPTURADA</b> com sucesso para estudo de bio-anatomia na Base-04.<br><br>
                    <b>Baixas/Danos:</b> Nenhuma baixa na equipe. Três estudantes que ouviram os sussurros iniciais através das frestas sofreram síncope e foram tratados com amnésicos Classe C.
                </div>
                """, unsafe_allow_html=True)
            elif senha_log2:
                st.error("Chave incorreta. Tentativa de violação registrada no Terminal Central.")

        st.write("")

        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-06B</b></span><br>
            <b>Localização:</b> Perímetro do Acidente [CONFIDENCIAL] - Posto de Observação Avançado<br>
            <b>Status da Missão:</b> Ativa / Monitoramento Crítico<br>
            <b>Descrição Básica:</b> Detectado aumento na pressão atmosférica indicando movimentação de energia de espectro vermelho. Patrulhas de Caçadores foram posicionadas. <span class="tarja-censurada">FOI VISUALIZADA UMA ESTRUTURA BIOLÓGICA DE DETRITOS DE</span>. Risco iminente de exposição anômala.
        </div>
        """, unsafe_allow_html=True)
        
        exp_3 = st.expander("🔑 DESCRIPTOGRAFAR ARQUIVO EXP-2026-06B")
        with exp_3:
            senha_log3 = st.text_input("Insira a chave de decodificação tática (Log 3):", type="password", key="pwd_log3")
            if senha_log3 == "37\\18m-4X":
                st.markdown("""
                <div class="bloco-desbloqueado">
                    <span class="tag-verde">✔ ACESSO AUTORIZADO — PATENTE DIRETORIA</span><br><br>
                    <b>RELATÓRIO TÁTICO INTEGRAL:</b><br>
                    <b>Equipe de Incursão:</b> Caçador de Área <i>Carlos "Carcará" Mendes</i> (CA), Caçador de Área <i>Renato "Escudo" Borges</i> (CA) sob coordenação do Líder de Caça <i>Comandante Brandão</i> (LC).<br><br>
                    <b>Entidade Identificada:</b> Anomalia Territorial Classe 4 ("A Sentinela de Fuligem"). Uma entidade colossal semi-sólida composta por cinza inteligente e flutuações térmicas de espectro vermelho.<br><br>
                    <b>Resumo do Confronto:</b> Uma patrulha de reconhecimento de três Agentes Aprendizes (AA) cruzou a linha de demarcação por falha de navegação. A Sentinela ergueu-se do solo gerando uma tempestade de vácuo calcinante. A equipe de Caça de elite interveio para criar uma barreira de supressão psíquica e extrair os sobreviventes.<br><br>
                    <b>Desfecho:</b> A entidade não pôde ser morta nem capturada devido à sua escala geográfica. Missão classificada como <b>CONTIDA / MONITORAMENTO ATIVO</b>. O perímetro foi expandido em 5km de exclusão total.<br><br>
                    <b>Baixas/Danos:</b> <span class="tag-vermelha"><b>TRÊS ÓBITOS CONFIRMADOS</b></span> da equipe de triagem primária (Agentes Aprendizes desintegrados termicamente). O Caçador <i>Renato Borges</i> perdeu o braço direito devido à corrosão da fuligem espiritual. O Líder de Caça <i>Comandante Brandão</i> assumiu o comando do setor.
                </div>
                """, unsafe_allow_html=True)
            elif senha_log3:
                st.error("Chave incorreta. Tentativa de violação registrada no Terminal Central.")

    # --- DIRETÓRIO 6: ESPECIALIZAÇÕES DE AGENTES ---
    elif opcao == "Especializações de Agentes":
        st.subheader("DIRETÓRIO DE ESPECIALIZAÇÕES OPERACIONAIS")
        st.write("Consulta formal das classes e funções táticas dentro da estrutura da Fundação.")
        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="bloco-confidencial">
                <h4 style='color:#aa0000 !important;'>OCULTISTA</h4>
                <p><b>Classificação:</b> Especialista em Manipulação de Energia Espiritual.</p>
                <p>Agentes dotados de alta afinidade com o Sobrenatural. São responsáveis pela execução de rituais de estabilização e supressão de ameaças de nível Vetorial. Sua presença é fundamental para a preservação da barreira da realidade, sendo o elo mais próximo com as forças que tentamos conter.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="bloco-confidencial">
                <h4 style='color:#aa0000 !important;'>MÉDICO</h4>
                <p><b>Classificação:</b> Pilar de Suporte e Salvaguarda Vital.</p>
                <p>Peça fundamental em qualquer equipe de campo. O médico é o responsável pela manutenção da integridade biológica da unidade. Devido ao seu papel insubstituível na sobrevivência da equipe, este agente possui prioridade máxima de proteção em cenários de combate.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="bloco-confidencial">
                <h4 style='color:#aa0000 !important;'>COMBATENTE</h4>
                <p><b>Classificação:</b> Unidade de Choque e Táticas de Contenção.</p>
                <p>Agentes especializados em intervenção direta. Seja através da maestria com lâminas, combate corpo a corpo ou técnicas de impacto, o combatente é a força tática de elite. Responsáveis pela neutralização física de ameaças, operam como a linha de frente defensiva e ofensiva da organização.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="bloco-confidencial">
                <h4 style='color:#aa0000 !important;'>MECÂNICO</h4>
                <p><b>Classificação:</b> Suporte Técnico e Engenharia de Campo.</p>
                <p>Especialistas em logística, manutenção de equipamentos de alta complexidade e reparos de emergência. A habilidade motora e o conhecimento técnico do mecânico garantem que nossa infraestrutura tecnológica e armamentos especializados funcionem sob condições adversas de campo.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.info("Nota: A designação de classe é permanente após a conclusão do treinamento básico. Alterações requerem autorização expressa da Diretoria.")

    # --- DIRETÓRIO 7: GERADOR DE CREDENCIAL TÁTICA ---
    elif opcao == "Gerador de Credencial Tática":
        st.subheader("MÓDULO DE EMISSÃO DE IDENTIDADE FUNCIONAL")
        st.write("Gere o cartão de acesso digital criptografado para os agentes em campo operando na comunidade.")
        st.write("---")
        
        col_inp1, col_inp2 = st.columns(2)
        with col_inp1:
            nome_agente = st.text_input("Nome de Registro do Agente:", placeholder="Ex: Denis Amorim")
            alocacao_base = st.text_input("Setor / Base de Operação:", placeholder="Ex: São Miguel dos Antares")
        
        with col_inp2:
            grau_selecionado = st.selectbox("Nível de Liberação (Patente):", [
                "Nível 1 - AT (Agente em Treinamento)",
                "Nível 2 - AA (Agente Aprendiz)",
                "Nível 3 - AB (Agente Básico)",
                "Nível 4 - AC (Agente de Campo)",
                "Nível 5 - CT (Caçador em Treinamento)",
                "Nível 6 - CA (Caçador de Área)",
                "Nível 7 - LC (Líder de Caça)"
            ])
            assinatura_digital = st.text_input("Código de Assinatura Funcional (Identificador):", placeholder="Ex: AC-908\\4F")

        st.write("")
        
        if nome_agente:
            # Puxamos as tags HTML totalmente para a esquerda para evitar o bug do bloco cinza
            st.markdown(f"""
<div class="badge-container">
<div class="badge-header">
<span class="badge-title-cn">COALIZÃO PARAMILITAR CRUZ NEGRA</span><br>
<span class="badge-subtitle-cn">CREDENCIAL DE IDENTIFICAÇÃO DE CAMPO</span>
</div>
<p class="badge-label">NOME OPERACIONAL: <span class="badge-value">{nome_agente.upper()}</span></p>
<p class="badge-label">PATENTE / GRAU: <span class="badge-value">{grau_selecionado}</span></p>
<p class="badge-label">BASE DE SUPORTE: <span class="badge-value">{alocacao_base.upper() if alocacao_base else 'NÃO CATALOGADA'}</span></p>
<p class="badge-label">LOGISTICA VETORIAL: <span class="badge-value" style="color:#8b0000 !important;">ATIVADA (2012)</span></p>
<div class="badge-footer">ESTE DOCUMENTO É PROPRIEDADE INALIENÁVEL DA CRUZ NEGRA. O PORTADOR ESTÁ AUTORIZADO A REQUISITAR SUPRIMENTOS, ALOCAÇÃO DE EQUIPES DE INFRAESTRUTURA E COMANDO DE OPERAÇÕES DE APAGAMENTO LOCAL. EM CASO DE QUEBRA DE SANIDADE, ESTA CREDENCIAL DEVE SER COLETADA E O MATERIAL ORGÂNICO DO AGENTE PROCESSADO.<br><br><span style="font-weight:bold; color:#000000;">ASSINATURA ELETRÔNICA: {assinatura_digital if assinatura_digital else 'AUTENTICADA'}</span></div>
</div>
""", unsafe_allow_html=True)
    # --- NOVO DIRETÓRIO: GERENCIADOR DE FICHA ATIVA ---
    elif opcao == "Gerenciador de Ficha Ativa":
        import json # Garante que a biblioteca JSON está importada para o save

        st.subheader("🗃️ PROTOCOLO DE MONITORAMENTO DE AGENTE")
        st.write("Ficha tática operacional otimizada para campanhas com rolagens físicas de dados.")
        st.write("---")

        # Inicializando os estados de sessão de forma isolada
        if 'hp_atual' not in st.session_state: st.session_state.hp_atual = 30
        if 'energia_atual' not in st.session_state: st.session_state.energia_atual = 15
        if 'sanidade_atual' not in st.session_state: st.session_state.sanidade_atual = 10

        # Funções de Callback estritas para evitar interferência entre os botões
        def mudar_hp(valor): st.session_state.hp_atual += valor
        def mudar_pe(valor): st.session_state.energia_atual += valor
        def mudar_san(valor): st.session_state.sanidade_atual += valor

        # --- SISTEMA DE CARREGAMENTO DE FICHA (UPLOAD) ---
        # Fica no topo para capturar o arquivo antes de renderizar os inputs
        st.markdown("<p style='color:#ef4444; font-weight:bold; margin-bottom:2px;'>💾 ARQUIVAMENTO EXTERNO</p>", unsafe_allow_html=True)
        arquivo_carregado = st.file_uploader("Para continuar de onde parou, arraste o arquivo .json da sua ficha aqui:", type=["json"], key="uploader_ficha")
        
        if arquivo_carregado is not None:
            try:
                dados_carregados = json.load(arquivo_carregado)
                
                # Injetando os dados carregados de volta no session_state do Streamlit
                st.session_state.hp_atual = dados_carregados.get("hp_atual", 30)
                st.session_state.energia_atual = dados_carregados.get("energia_atual", 15)
                st.session_state.sanidade_atual = dados_carregados.get("sanidade_atual", 10)
                
                # Injetando os valores dos inputs e caixas de texto usando suas chaves (keys)
                st.session_state["nome_pc"] = dados_carregados.get("nome", "Abel")
                st.session_state["inv_box"] = dados_carregados.get("inventario", "")
                st.session_state["rit_box"] = dados_carregados.get("rituais", "")
                st.session_state["anot_box"] = dados_carregados.get("anotacoes", "")
                
                # Injetando Atributos
                st.session_state["at_forca"] = dados_carregados.get("at_forca", 4)
                st.session_state["at_res"] = dados_carregados.get("at_res", 4)
                st.session_state["at_vig"] = dados_carregados.get("at_vig", 2)
                st.session_state["at_ref"] = dados_carregados.get("at_ref", 1)
                st.session_state["at_fur"] = dados_carregados.get("at_fur", 2)
                st.session_state["at_pre"] = dados_carregados.get("at_pre", 1)
                st.session_state["at_int"] = dados_carregados.get("at_int", 1)
                st.session_state["at_log"] = dados_carregados.get("at_log", 2)
                st.session_state["at_ocu"] = dados_carregados.get("at_ocu", 0)
                st.session_state["at_von"] = dados_carregados.get("at_von", 2)
                st.session_state["at_f_san"] = dados_carregados.get("at_f_san", 1)
                st.session_state["at_prs"] = dados_carregados.get("at_prs", 1)
                
                # Injetando Perícias Salvas
                pericias_salvas = dados_carregados.get("pericias", {})
                lista_pericias_oficiais = ["ARMAS BRANCAS", "ROUBO", "ESQUIVA", "MECANICA", "PILOTAGEM", "ARMAS DE FOGO", "SOBREVIVENCIA", "MEDICINA", "VITALIDADE", "RITUAIS", "ARCANISMO", "ARRUMAÇÃO"]
                
                for pericia in lista_pericias_oficiais:
                    chave_pericia = f"per_{pericia.lower().replace(' ', '_')}"
                    nivel_salvo = pericias_salvas.get(pericia, "Não Treinada")
                    
                    # Converte o nome limpo de volta para a string exata do st.radio
                    if nivel_salvo == "Nível I": mapa_nivel = "Nível I (1)"
                    elif nivel_salvo == "Nível II": mapa_nivel = "Nível II (2)"
                    elif nivel_salvo == "Nível III": mapa_nivel = "Nível III (3)"
                    else: mapa_nivel = "Não Treinada (Nível 0)"
                    
                    st.session_state[chave_pericia] = mapa_nivel
                    
                st.success("📂 Prontuário sincronizado com sucesso! Dados restaurados.")
            except Exception as e:
                st.error(f"❌ Erro ao ler o arquivo de Prontuário: {e}")

        st.write("---")

        # --- SEÇÃO DE IDENTIFICAÇÃO GERAL ---
        st.markdown("<p style='color:#ef4444; font-weight:bold; margin-bottom:2px;'>IDENTIFICAÇÃO OPERACIONAL</p>", unsafe_allow_html=True)
        col_id1, col_id2, col_id3 = st.columns([2, 1, 1])
        with col_id1:
            nome_personagem = st.text_input("Nome do Agente:", key="nome_pc")
        with col_id2:
            # Vinculamos as chaves para salvar o estado delas também de tabela
            classe_selecionada = st.selectbox("Classe / Função:", ["Combatente", "Especialista / Suporte", "Médico", "Ocultista"], key="classe_sel")
        with col_id3:
            nivel_selecionado = st.selectbox("Nível / Patente:", ["Nível 1 (AT)", "Nível 2 (AA)", "Nível 3 (AB)", "Nível 4 (AC)", "Nível 5 (CT)", "Nível 6 (CA)", "Nível 7 (LC)"], key="nivel_sel")

        st.write("---")

        # --- SEÇÃO VITAIS ESTILIZADA ---
        st.markdown("<p style='color:#ef4444; font-weight:bold; text-align:center; margin-bottom:15px;'>STATUS VITAIS ATIVOS</p>", unsafe_allow_html=True)
        
        col_v1, col_v2, col_v3 = st.columns(3)
        
        with col_v1:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #2d1313, #1e0b0b); border: 2px solid #ef4444; border-radius: 10px; padding: 15px; text-align: center; box-shadow: 0px 4px 10px rgba(239, 68, 68, 0.2);">
                    <span style="color: #f87171; font-weight: bold; font-size: 14px;">PONTOS DE VIDA (HP)</span>
                    <h1 style="color: #ef4444; margin: 10px 0; font-size: 42px; font-family: 'Courier New', monospace;">{st.session_state.hp_atual}</h1>
                </div>
                """, unsafe_allow_html=True
            )
            st.write("")
            cb1, cb2 = st.columns(2)
            with cb1: st.button("➖ HP", key="btn_sub_hp", on_click=mudar_hp, args=(-1,), use_container_width=True)
            with cb2: st.button("➕ HP", key="btn_add_hp", on_click=mudar_hp, args=(1,), use_container_width=True)
                
        with col_v2:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #0f2430, #0a1720); border: 2px solid #0ea5e9; border-radius: 10px; padding: 15px; text-align: center; box-shadow: 0px 4px 10px rgba(14, 165, 233, 0.2);">
                    <span style="color: #7dd3fc; font-weight: bold; font-size: 14px;">ENERGIA COMPLEMENTAR (PE)</span>
                    <h1 style="color: #0ea5e9; margin: 10px 0; font-size: 42px; font-family: 'Courier New', monospace;">{st.session_state.energia_atual}</h1>
                </div>
                """, unsafe_allow_html=True
            )
            st.write("")
            cb3, cb4 = st.columns(2)
            with cb3: st.button("➖ PE", key="btn_sub_pe", on_click=mudar_pe, args=(-1,), use_container_width=True)
            with cb4: st.button("➕ PE", key="btn_add_pe", on_click=mudar_pe, args=(1,), use_container_width=True)

        with col_v3:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #0d2219, #081610); border: 2px solid #10b981; border-radius: 10px; padding: 15px; text-align: center; box-shadow: 0px 4px 10px rgba(16, 185, 129, 0.2);">
                    <span style="color: #6ee7b7; font-weight: bold; font-size: 14px;">SANIDADE OPERACIONAL (SAN)</span>
                    <h1 style="color: #10b981; margin: 10px 0; font-size: 42px; font-family: 'Courier New', monospace;">{st.session_state.sanidade_atual}</h1>
                </div>
                """, unsafe_allow_html=True
            )
            st.write("")
            cb5, cb6 = st.columns(2)
            with cb5: st.button("➖ SAN", key="btn_sub_san", on_click=mudar_san, args=(-1,), use_container_width=True)
            with cb6: st.button("➕ SAN", key="btn_add_san", on_click=mudar_san, args=(1,), use_container_width=True)

        st.write("---")

        # --- SEÇÃO MATRIZ DE ATRIBUTOS COM TETO EM 15 ---
        st.markdown("<p style='color:#ef4444; font-weight:bold;'>MATRIZ DE CAPACIDADES E ATRIBUTOS</p>", unsafe_allow_html=True)
        st.write("Insira os valores das ramificações (Máximo 15). A categoria calculará automaticamente o dado de teste.")

        def determinar_dado_sistema(valor_total):
            if valor_total <= 2: return "1d6"
            elif valor_total <= 5: return "1d8"
            elif valor_total <= 8: return "1d10"
            else: return "1d12"

        col_at1, col_at2 = st.columns(2)

        with col_at1:
            # Conjunto CORPO
            st.markdown("<div style='background-color:#1e1e24; padding:5px; border-radius:3px; font-weight:bold; color:#f87171;'>💪 CATEGORIA: CORPO</div>", unsafe_allow_html=True)
            f_forca = st.number_input("Força:", min_value=0, max_value=15, key="at_forca")
            f_res = st.number_input("Resistência:", min_value=0, max_value=15, key="at_res")
            f_vig = st.number_input("Vigor:", min_value=0, max_value=15, key="at_vig")
            soma_corpo = f_forca + f_res + f_vig
            dado_corpo = determinar_dado_sistema(soma_corpo)
            st.markdown(f"<p style='color:#f87171; font-weight:bold; font-size:15px;'>Soma Total CORPO: {soma_corpo} <span style='color:#94a3b8;'>({dado_corpo})</span></p>", unsafe_allow_html=True)
            st.write("")

            # Conjunto AGILIDADE
            st.markdown("<div style='background-color:#141f26; padding:5px; border-radius:3px; font-weight:bold; color:#38bdf8;'>⚡ CATEGORIA: AGILIDADE</div>", unsafe_allow_html=True)
            f_ref = st.number_input("Reflexos:", min_value=0, max_value=15, key="at_ref")
            f_fur = st.number_input("Furtividade:", min_value=0, max_value=15, key="at_fur")
            f_pre = st.number_input("Precisão:", min_value=0, max_value=15, key="at_pre")
            soma_agi = f_ref + f_fur + f_pre
            dado_agi = determinar_dado_sistema(soma_agi)
            st.markdown(f"<p style='color:#38bdf8; font-weight:bold; font-size:15px;'>Soma Total AGILIDADE: {soma_agi} <span style='color:#94a3b8;'>({dado_agi})</span></p>", unsafe_allow_html=True)

        with col_at2:
            # Conjunto MENTE
            st.markdown("<div style='background-color:#1b1924; padding:5px; border-radius:3px; font-weight:bold; color:#c084fc;'>🧠 CATEGORIA: MENTE</div>", unsafe_allow_html=True)
            f_int = st.number_input("Intelecto:", min_value=0, max_value=15, key="at_int")
            f_log = st.number_input("Lógica:", min_value=0, max_value=15, key="at_log")
            f_ocu = st.number_input("Ocultismo:", min_value=0, max_value=15, key="at_ocu")
            soma_mente = f_int + f_log + f_ocu
            dado_mente = determinar_dado_sistema(soma_mente)
            st.markdown(f"<p style='color:#c084fc; font-weight:bold; font-size:15px;'>Soma Total MENTE: {soma_mente} <span style='color:#94a3b8;'>({dado_mente})</span></p>", unsafe_allow_html=True)
            st.write("")

            # Conjunto FÉ
            st.markdown("<div style='background-color:#13201a; padding:5px; border-radius:3px; font-weight:bold; color:#34d399;'>⛪ CATEGORIA: FÉ</div>", unsafe_allow_html=True)
            f_von = st.number_input("Vontade:", min_value=0, max_value=15, key="at_von")
            f_san = st.number_input("Sanidade (Atrib):", min_value=0, max_value=15, key="at_f_san")
            f_prs = st.number_input("Presença:", min_value=0, max_value=15, key="at_prs")
            soma_fe = f_von + f_san + f_prs
            dado_fe = determinar_dado_sistema(soma_fe)
            st.markdown(f"<p style='color:#34d399; font-weight:bold; font-size:15px;'>Soma Total FÉ: {soma_fe} <span style='color:#94a3b8;'>({dado_fe})</span></p>", unsafe_allow_html=True)

        st.write("---")

        # --- SEÇÃO GRADE DE PERÍCIAS DETALHADAS ---
        st.markdown("<p style='color:#ef4444; font-weight:bold;'>🗂️ GRADE DE PERÍCIAS OPERACIONAIS</p>", unsafe_allow_html=True)
        
        lista_pericias_oficiais = [
            "ARMAS BRANCAS", "ROUBO", "ESQUIVA", "MECANICA", "PILOTAGEM", 
            "ARMAS DE FOGO", "SOBREVIVENCIA", "MEDICINA", "VITALIDADE", 
            "RITUAIS", "ARCANISMO", "ARRUMAÇÃO"
        ]

        col_p1, col_p2 = st.columns(2)
        pericias_treinadas_usuario = {}
        
        for idx, per in enumerate(lista_pericias_oficiais):
            target_col = col_p1 if idx % 2 == 0 else col_p2
            with target_col:
                escolha = st.radio(f"**{per}**", ["Não Treinada (Nível 0)", "Nível I (1)", "Nível II (2)", "Nível III (3)"], key=f"per_{per.lower().replace(' ', '_')}", horizontal=True)
                if escolha != "Não Treinada (Nível 0)":
                    pericias_treinadas_usuario[per] = escolha.split(" (")[0]

        st.write("---")

        # --- SEÇÃO INVENTÁRIO, RITUAIS LIVRES E ANOTAÇÕES GERAIS ---
        col_low1, col_low2 = st.columns(2)
        
        with col_low1:
            st.markdown("<p style='color:#ef4444; font-weight:bold; margin-bottom:2px;'>📥 INVENTÁRIO TÁTICO & CARGA</p>", unsafe_allow_html=True)
            inventario_texto = st.text_area("Slots e Equipamentos atuais:", placeholder="Itens e armas equipados...", height=120, key="inv_box")
            
            st.markdown("<p style='color:#ef4444; font-weight:bold; margin-bottom:2px; margin-top:15px;'>🔮 MANIFESTAÇÕES E RITUAIS CONHECIDOS</p>", unsafe_allow_html=True)
            rituais_texto = st.text_area("Descreva livremente rituais conhecidos, efeitos e custos de PE:", placeholder="Rituais conhecidos...", height=120, key="rit_box")

        with col_low2:
            st.markdown("<p style='color:#ef4444; font-weight:bold; margin-bottom:2px;'>📝 DIÁRIO DE CAMPO (ANOTAÇÕES CONFIDENCIAIS)</p>", unsafe_allow_html=True)
            anotacoes_texto = st.text_area("Registre pistas, nomes de sobreviventes e informações da campanha:", placeholder="Notas gerais da mesa...", height=292, key="anot_box")

        st.write("---")

        # --- NOVO BLOCO: EXPORTADOR DE FICHA (BOTÃO DE SALVAR) ---
        st.markdown("<p style='color:#ef4444; font-weight:bold;'>💾 EXPORTAR PRONTUÁRIO DE CAMPO</p>", unsafe_allow_html=True)
        st.write("Clique abaixo para fazer o download do arquivo de backup. Salve-o no seu computador e use o campo no topo da página para carregá-lo na próxima sessão.")
        
        # Estrutura JSON compacta com tudo o que está na tela no exato momento
        dados_exportar = {
            "nome": nome_personagem,
            "classe": classe_selecionada,
            "nivel": nivel_selecionado,
            "hp_atual": st.session_state.hp_atual,
            "energia_atual": st.session_state.energia_atual,
            "sanidade_atual": st.session_state.sanidade_atual,
            "at_forca": f_forca,
            "at_res": f_res,
            "at_vig": f_vig,
            "at_ref": f_ref,
            "at_fur": f_fur,
            "at_pre": f_pre,
            "at_int": f_int,
            "at_log": f_log,
            "at_ocu": f_ocu,
            "at_von": f_von,
            "at_f_san": f_san,
            "at_prs": f_prs,
            "pericias": pericias_treinadas_usuario,
            "inventario": inventario_texto,
            "rituais": rituais_texto,
            "anotacoes": anotacoes_texto
        }
        
        json_string = json.dumps(dados_exportar, indent=4, ensure_ascii=False)
        nome_arquivo_slug = nome_personagem.lower().replace(" ", "_") if nome_personagem else "agente"
        
        # Cria o botão de download oficial do Streamlit
        st.download_button(
            label="💾 Baixar Arquivo da Ficha (.json)",
            data=json_string,
            file_name=f"prontuario_{nome_arquivo_slug}.json",
            mime="application/json",
            use_container_width=True
            # O layout fica elegante cobrindo a largura do container
        )

        st.write("---")

        # --- SEÇÃO VISUAL: FOLHA DE FICHA TÁTICA ATUALIZADA (HTML SEGURO) ---
        st.markdown("<p style='color:#ef4444; font-weight:bold;'>📇 FOLHA DE MONITORAMENTO TÁTICO (IMAGEM DA FICHA)</p>", unsafe_allow_html=True)
        st.write("Abaixo está o documento oficial da sua ficha ativa estruturado dinamicamente para exibição limpa:")

        # CÁLCULO DINÂMICO DE COMBATE BASEADO NAS REGRAS
        dano_base = f_forca + 2
        resistencia_base = f_res + 2

        # Construindo as perícias formatadas em HTML
        html_pericias = ""
        if pericias_treinadas_usuario:
            html_pericias += "<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 6px; padding-left: 10px; color: #1e293b; font-size: 13px; font-family: sans-serif;'>"
            for p_nome, p_nivel in pericias_treinadas_usuario.items():
                html_pericias += f"<div>• <b>{p_nome}:</b> {p_nivel}</div>"
            html_pericias += "</div>"
        else:
            html_pericias = "<p style='margin: 0; font-size: 13px; color: #64748b; font-style: italic; font-family: sans-serif;'>Nenhuma perícia treinada ativa.</p>"

        # String HTML limpa
        card_html = f"""
        <div style="background-color: #ffffff; border: 3px solid #1e293b; border-radius: 6px; padding: 20px; font-family: Arial, sans-serif; color: #1e293b; box-sizing: border-box;">
            
            <div style="border-bottom: 2px solid #1e293b; padding-bottom: 10px; margin-bottom: 15px; text-align: center;">
                <h2 style="color: #1e293b; margin: 0; font-size: 18px; font-weight: bold; letter-spacing: 1px;">ORGANIZAÇÃO CRUZ NEGRA</h2>
                <p style="margin: 3px 0 0 0; font-size: 11px; color: #475569; font-weight: bold; letter-spacing: 3px;">PRONTUÁRIO DE IDENTIFICAÇÃO DE AGENTE</p>
            </div>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 15px; font-size: 14px; color: #1e293b;">
                <tr>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1; width: 50%;"><b>AGENTE COGNODOMINADO:</b> <span style="text-transform: uppercase;">{nome_personagem if nome_personagem else 'NÃO DECLARADO'}</span></td>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1;"><b>STATUS DE CAPACIDADE VITAL (HP):</b> <span style="color: #dc2626; font-weight: bold;">{st.session_state.hp_atual}</span></td>
                </tr>
                <tr>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1;"><b>FUNÇÃO OPERACIONAL:</b> {classe_selecionada}</td>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1;"><b>RESERVA ENERGÉTICA (PE):</b> <span style="color: #0284c7; font-weight: bold;">{st.session_state.energia_atual}</span></td>
                </tr>
                <tr>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1;"><b>PATENTE DE CAMPO:</b> {nivel_selecionado}</td>
                    <td style="padding: 6px 0; border-bottom: 1px dashed #cbd5e1;"><b>INTEGRIDADE COGNITIVA (SAN):</b> <span style="color: #16a34a; font-weight: bold;">{st.session_state.sanidade_atual}</span></td>
                </tr>
            </table>
            
            <div style="background-color: #f1f5f9; border: 1px solid #cbd5e1; padding: 10px; border-radius: 4px; margin-bottom: 10px;">
                <p style="margin: 0; font-size: 11px; font-weight: bold; color: #475569; text-align: center; letter-spacing: 1px;">
                    MATRIZ DE DADOS ATIVOS SINDICALIZADOS
                </p>
                <p style="margin: 5px 0 0 0; font-size: 13px; color: #0f172a; text-align: center; font-weight: bold;">
                    CORPO: {soma_corpo} ({dado_corpo}) | AGILIDADE: {soma_agi} ({dado_agi}) | MENTE: {soma_mente} ({dado_mente}) | FÉ: {soma_fe} ({dado_fe})
                </p>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 15px;">
                <div style="background-color: #fef2f2; border: 1px solid #fee2e2; padding: 8px; border-radius: 4px; text-align: center;">
                    <span style="font-size: 11px; font-weight: bold; color: #991b1b; letter-spacing: 0.5px;">⚔️ MODIFICADOR DE DANO</span>
                    <p style="margin: 3px 0 0 0; font-size: 15px; font-weight: bold; color: #dc2626;">+{dano_base} (Força + 2)</p>
                </div>
                <div style="background-color: #f0fdf4; border: 1px solid #dcfce7; padding: 8px; border-radius: 4px; text-align: center;">
                    <span style="font-size: 11px; font-weight: bold; color: #166534; letter-spacing: 0.5px;">🛡️ RESISTÊNCIA A DANO</span>
                    <p style="margin: 3px 0 0 0; font-size: 15px; font-weight: bold; color: #16a34a;">{resistencia_base} (Resistência + 2)</p>
                </div>
            </div>
            
            <div style="border: 1px solid #cbd5e1; padding: 12px; border-radius: 4px; background-color: #f8fafc; margin-bottom: 15px;">
                <p style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #475569; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; letter-spacing: 0.5px;">
                    📜 CAPACITAÇÕES TÉCNICAS HOMOLOGADAS (PERÍCIAS TREINADAS)
                </p>
                {html_pericias}
            </div>
            
            <div style="margin-top: 15px; border-top: 1px solid #1e293b; padding-top: 5px; text-align: right;">
                <p style="margin: 0; font-size: 9px; color: #64748b; font-style: italic;">Autenticação Interface C.A.I.M. — Documento de Uso Estrito Institucional.</p>
            </div>
        </div>
        """
        
        st.components.v1.html(card_html, height=600, scrolling=False)
        st.write("")

    # --- NOVO DIRETÓRIO SECRETO: MARCO 96 (CORREÇÃO DE PARSING) ---
    elif opcao == "Relatório de Falha Sistêmica: Marco 96":
        st.markdown("""
        <div style='background-color: #020617; padding: 25px; border-radius: 8px; border: 2px solid #ef4444; box-shadow: 0 0 15px rgba(239, 68, 68, 0.2);'>
            <h3 style='color: #ef4444 !important; font-family: "Courier New", Courier, monospace; margin: 0;'>⚠️ SINAL DE ALERTA: PROTOCOLO RESTRITO DE ARQUIVAMENTO</h3>
            <p style='color: #94a3b8 !important; font-family: "Courier New", Courier, monospace; font-size: 13px;'>
                Você está tentando acessar uma partição redundante e expurgada da Controladoria Central (Index: 1996). 
                Esta documentação detalha a maior quebra de sigilo operacional registrada na história desta instituição. Entrada não autorizada disparará o Protocolo de Saneamento.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        senha_arquivo = st.text_input("Insira o Código de Quebra de Protocolo (Assinatura Entidade):", type="password", key="senha_secreta_1996")
        
        if senha_arquivo:
            if senha_arquivo == "C.A.I.M." or senha_arquivo.upper() == "CAIM":
                
                container_log = st.empty()
                with container_log.container():
                    st.markdown("<p style='color:#10b981; font-family:monospace;'>[SISTEMA] Injetando assinatura espiritual C.A.I.M. no bypass...</p>", unsafe_allow_html=True)
                    time.sleep(0.7)
                    st.markdown("<p style='color:#10b981; font-family:monospace;'>[SISTEMA] Quebrando barreiras de proteção de São Miguel...</p>", unsafe_allow_html=True)
                    time.sleep(0.9)
                    st.markdown("<p style='color:#ef4444; font-family:monospace;'>[ALERTA] Rastreamento de retina temporariamente obscurecido.</p>", unsafe_allow_html=True)
                    time.sleep(0.5)
                    st.markdown("<p style='color:#10b981; font-family:monospace;'>[SISTEMA] Recuperando registros de falha catastrófica de 1996...</p>", unsafe_allow_html=True)
                    time.sleep(1.2)
                
                container_log.empty()
                
                # HTML totalmente alinhado à esquerda para evitar que o Streamlit interprete como bloco de código
                st.markdown("""<style>
.log-text { font-family: 'Courier New', Courier, monospace; font-size: 14px; line-height: 1.6; color: #e2e8f0 !important; }
.sub-titulo-log { color: #f87171 !important; font-family: 'Courier New', monospace; font-weight: bold; margin-top: 20px; border-bottom: 1px dashed #ef4444; padding-bottom: 5px; }
.tarja-preta { background-color: #ffffff; color: #ffffff; padding: 0 4px; border-radius: 2px; }
</style>
<div style='background-color: #0f172a; padding: 25px; border-radius: 8px; border-left: 5px solid #ef4444;'>
<h2 style='color: #ef4444 !important; font-family: "Courier New", monospace; text-align: center;'>ARQUIVOS DE INCIDENTE: O ARREBATAMENTO (MARCO 96)</h2>
<p style='text-align: center; color: #64748b !important; font-family: monospace; font-size: 11px;'>STATUS: RECONSTRUÇÃO ILEGAL // GRAU DE SEGREDO: IMPERIAL (MUNDO REVELADO)</p>
<hr style='border-color: #334155;'>
<div class="log-text">
<p><b>DATA DO REGISTRO ORIGINAL:</b> Novembro de 1996<br>
<b>CLASSIFICAÇÃO DO EVENTO:</b> Quebra de Realidade Escala-5 (Global)<br>
<b>DIRETRIZ CRUCIAL:</b> Apagamento total de menções públicas no ano corrente de 2012.</p>
<h4 class="sub-titulo-log">1. O MARCO ZERO: O CLARÃO E O PARADOXO CRONOLÓGICO</h4>
<p>O evento global denominado <b>"Arrebatamento"</b> teve início operacional após o desaparecimento do espécime <span class="tarja-preta">BILLY</span>, herdeiro dinástico de alta relevância financeira. Investigações de campo confirmaram a interceptação de uma correspondência anacrônica enviada de um vetor temporal futuro, gerando um colapso de causalidade na linha temporal padrão. No zênite do evento, o espécime flutuou espontaneamente, atuando como chave de ignição que expôs o sobrenatural em escala mundial.</p>
<h4 class="sub-titulo-log">2. A SÍNDROME NEURAL DOS OLHOS BRANCOS</h4>
<p>Após o clarão do Arrebatamento, registrou-se uma mutação ocular síncrona em massa por toda a população global. Os indivíduos afetados desenvolviam despigmentação total da íris e da esclera (<b>Olhos Brancos</b>). Relatórios analíticos posteriores confirmaram que esta condição transformava os hospedeiros em terminais de transmissão biológica para a entidade albina conhecida como <b>"O Sete Olhos"</b>. Cada par de olhos brancos permitia à criatura observar o mundo exterior de forma irrestrita.
<br><i>Nota de Prontuário:</i> O agente de campo <span class="tarja-preta">ABEL</span> exibia a reação de olhos brancos reflexivamente ao acessar memórias do Arrebatamento, tornando-se um vetor de espionagem passiva do inimigo.</p>
<h4 class="sub-titulo-log">3. AS CALAMIDADES AMBIENTAIS DE BELZEBU</h4>
<p>A manifestation física da Entidade Vermelha (Belzebu) em solo sagrado quebrou permanentemente a capacidade de contenção velada da Cruz Negra devido aos seus efeitos macroecológicos globais:</p>
<ul>
<li><b>Vetor Botânico (Flora de Espinhos):</b> Crescimento exponencial de bio-redomas espinhosas por todo o planeta. A vegetação anômala utilizava hemoglobina como combustível principal; qualquer contato com sangue humano multiplicava a massa vegetal em progressão geométrica imediata.</li>
<li><b>Vetor Climático (Chuva de Sangue e Nevoeiro):</b> Precipitação hemática seguida por uma névoa densa permanente. O fenômeno meteorológico trouxe consigo entidades mímicas (<b>Doppelgangers</b>), especializadas em emular perfeitamente a biologia, voz e memórias dos agentes para fins de infiltração e eliminação tática.</li>
</ul>
<h4 class="sub-titulo-log">4. DOSSIÊ DE INFECTADOS E BAIXAS DE CAMPANHA</h4>
<p><b>SUJEITO: <span class="tarja-preta">Antonio</span> (Médico Operacional)</b><br>
Status: Falha Crítica / Transmutação Classe-Diptera. Após ceder à coação e apertar a mão de Belzebu, o indivíduo sofreu degeneração celular severa, transmutando-se em uma entidade híbrida insectoide (Mosca Humanoide). Sob controle sináptico da entidade, recebeu ordens diretas de executar todos os membros remanescentes de sua unidade de apoio.</p>
<p><b>SUJEITO: <span class="tarja-preta">Abel</span> (Linhagem Híbrida / Lilith)</b><br>
Status: Eliminado por Trauma Físico. Detentor de herança genética ligada à entidade Lilith. Teve sua fração de alma demoníaca extraída e manipulada em contrato firmado com a entidade Caim. No clímax do Incidente, operou como uma marionete de combate direta de Caim contra o transmutado <span class="tarja-preta">Antonio</span>. Sobreviveu ao confronto direto, mas foi sumariamente executado pelo espécime <span class="tarja-preta">BILLY</span> ao fim do colapso.</p>
<h4 class="sub-titulo-log">5. O PROJETO ASMODEUS</h4>
<p>Registros recuperados do útero tático da combatente <span class="tarja-preta">TAKIMO</span> revelaram uma inseminação induzida pela criatura de Sete Olhos. O feto gerado continha o sequenciamento bio-espiritual de Asmodeus, arquitetado como uma arma biológica com o único propósito de rivalizar, combater e neutralizar o avanço de Belzebu na Terra.</p>
<p style='color: #ef4444 !important; font-weight: bold; margin-top: 15px;'>[ALERTA CENTRAL 2012]: O Incidente de 1996 causou a revelação pública do Sobrenatural e o pânico civilizatório subsequente. Qualquer vazamento destes dados da nossa Intranet Administrativa resultará em execução sumária por quebra de sigilo institutional.</p>
</div>
</div>""", unsafe_allow_html=True)
                
            else:
                st.error("❌ Código de Acesso Inválido. Tentativa de infiltração reportada à Diretora Carter.")