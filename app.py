import streamlit as st
import time
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal de Acesso Integrado", page_icon="🏢", layout="wide")

# 2. CONTROLE DE ACESSO
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

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

# ==========================================
# FASE 1: TELA DE FACHADA (CORPORATIVA)
# ==========================================
if not st.session_state['autenticado']:
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
            <p style='margin:0; font-size:13px;'>Cessão e mapeamento de amplas áreas abertas e centros de treinamento para laboratórios e faculdades de Educação Física, garantindo espaço técnico seguro para atividades externas.</p>
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
            if usuario_input == "W" and senha_input == "24\\12k-0Y":
                with st.spinner("Descriptografando chaves de segurança..."):
                    time.sleep(2.5)
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Erro de autenticação: Credenciais inválidas ou nível de acesso insuficiente.")
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
            <p style='margin:0; font-size:13px;'>Identificadas anomalias estruturais e operacionais in em uma de nossas unidades de manufatura. Iniciado o protocolo padrão de retirada parcial de capital preventivo para contenção de danos e desvalorização estratégica controlada de ativos.</p>
        </div>
        <div class="card-noticia">
            <span class="data-noticia font-mono">DIRETRIZ DE REAQUISIÇÃO</span>
            <h4 style='margin:5px 0; font-size:14px; font-weight:bold;'>Retorno de Investimento Pós-Saneamento</h4>
            <p style='margin:0; font-size:13px;'>Após a intervenção de nossas equipes de auditoria de campo para a resolução dos problemas técnicos locais, o plano de recompra massiva de ações será executado, visando a estabilização e subsequente expansão econômica.</p>
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
        .tarja-preta {
            background-color: #000000;
            color: #000000;
            padding: 0 4px;
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
    
    opcao = st.sidebar.radio("Selecionar Arquivo:", [
        "Terminal Central / Diretoria",
        "Tratado de Ocultamento Sobrenatural",
        "Hierarquia e Níveis de Liberação",
        "Protocolos de Fé e Resiliência",
        "Relatórios de Expedição de Campo",
        "Transmissão C.A.I.M."
    ])

    # --- DIRETÓRIO 1: TERMINAL CENTRAL ---
    if opcao == "Terminal Central / Diretoria":
        st.subheader("TERMINAL DE COMANDO OPERACIONAL")
        st.write("Conexão estabelecida com o servidor Base-01. Sessão activa sob a identificação da Diretoria.")
        st.write("---")
        
        st.markdown(f"""
        <div class="bloco-confidencial">
            <p><b>Autoridade Máxima Atual:</b> Diretora Ana Carter</p>
            <p><b>Status da Infraestrutura:</b> <span style='color:#00ff00;'>ESTÁVEL</span></p>
            <p><b>Índice de Dissipação de Névoa:</b> Controlado dentro dos parâmetros de segurança da comunidade.</p>
            <br>
            <p><i>"A ignorância civil não é uma falha do nosso sistema, é o nosso maior produto. Mantemos a escuridão contida para que o mundo possa continuar caminhando sob a luz de uma falsa normalidade."</i><br>
            — <b>Diretora Ana Carter</b>, Pronunciamento no Conselho Superior.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- DIRETÓRIO 2: O QUE É A CRUZ NEGRA ---
    elif opcao == "Tratado de Ocultamento Sobrenatural":
        st.subheader("ARQUIVO DE ORIGEM: A NATUREZA DA ORGANIZAÇÃO")
        st.write("Documento datado de fundação institucional e retido para conhecimento ideológico.")
        st.write("---")
        st.write("""
        A **Cruz Negra** é uma coalizão paramilitar e científica global de caráter estritamente confidencial, operando à margem de governos soberanos. Nossa única e absoluta diretriz é a **neutralização, contenção e apagamento sistemático de manifestações sobrenaturais**, anomalias biológicas e perturbações da malha física que ameacem a estabilidade psicológica e social da humanidade.
        """)
        st.write("""
        O tecido da realidade é frágil e constantemente ameaçado por forças não catalogadas pela ciência convencional. Através da fachada civil *'Caridade e Regente Universitária do Zelo'*, a organização canaliza verbas de grandes conglomerados, adquire infraestruturas estratégicas (como laboratórios médicos e zonas de exclusão geográfica) e recruta indivíduos com perfis psicológicos resilientes para servirem na linha de frente como agentes de contenção.
        """)

    # --- DIRETÓRIO 3: GRAUS DOS AGENTES ---
    elif opcao == "Hierarquia e Níveis de Liberação":
        st.subheader("DOCUMENTO DE GESTÃO DE PESSOAL: GRAUS DE AGENTES")
        st.write("Abaixo estão listados os níveis de liberação tática e modificação biológica autorizados pela Diretora Ana Carter.")
        st.write("---")
        
        st.markdown("""
        <div class="bloco-confidencial">
            <p><b class="tag-vermelha">Nível 1 - AT (Agente em Treinamento):</b> Alocados na triagem e suporte periférico. Não possuem autorização para contato direto com anomalias de Classe Vetorial Ativa sem supervisão.</p>
            <p><b class="tag-vermelha">Nível 2 - AA (Agente Aprendiz):</b> Treinados em protocolos básicos de supressão psíquica. Autorizados a participar de perímetros de isolamento secundários.</p>
            <p><b class="tag-vermelha">Nível 3 - AB (Agente Básico):</b> Espinha dorsal tática da organização. Possuem estabilização psicológica comprovada e armamento adaptado para interferência de espectro leve.</p>
            <p><b class="tag-vermelha">Nível 4 - AC (Agente de Campo):</b> Veteranos de combate anômalo. Responsáveis pela liderança de incursões urbanas e aplicação imediata de protocolos de sigilo na comunidade.</p>
            <p><b class="tag-vermelha">Nível 5 - CT (Caçador em Treinamento):</b> Selecionados para o programa avançado de erradicação. Iniciam os testes de exposição direta à energia espiritual purificada.</p>
            <p><b class="tag-vermelha">Nível 6 - CA (Caçador de Área):</b> Destinados à contenção de anomalias territoriais massivas. Possuem autonomia tática para decretar quarentenas econômicas e físicas.</p>
            <p><b class="tag-vermelha">Nível 7 - LC (Líder de Caça):</b> O ápice operacional da Cruz Negra. Agentes modificados com alto grau de resiliência a distorções da reality, respondendo diretamente à Diretora Ana Carter.</p>
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
            <p>Caso uma das propriedades ou empresas controladas pelo Nicho Investidor apresente quebra de barreira física (ex: eventos de infestação em cadeias produtivas), o protocolo de liquidação deve ser ativado imediatamente. O desinvestimento artificial derruba o valor das ações, justificando o esvaziamento do local antes do envio da equipe de Caça.</p>
        </div>
        <div class="bloco-confidencial">
            <h4>Protocolo III — Contenção de Material Biológico Humano</h4>
            <p>O fornecimento de tecidos orgânicos para laboratórios parceiros sob a fachada de estudos de medicina deve seguir os critérios de eliminação de rastros de energia residual. Nenhum cadáver anômalo pode ser descartado em solo público sem a devida aplicação do reagente de cinzas.</p>
        </div>
        """, unsafe_allow_html=True)

    # # --- DIRETÓRIO 5: RELATÓRIOS DE EXPEDIÇÃO (COM SISTEMA DE SENHA INTERNA E NOMES EM PT-BR) ---
    elif opcao == "Relatórios de Expedição de Campo":
        st.subheader("LOGS DE MISSÕES DE CAMPO INTERCEPTADOS [SECRETO]")
        st.write("Registros históricos de incursões táticas autorizadas pela administração central. Requer senha criptográfica para visualização total.")
        st.write("---")
        
        # --- LOG 1 ---
        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-04A</b></span><br>
            <b>Localização:</b> Setor Industrial Sul - Fábrica de Processamento de Doces [CONFIDENCIAL]<br>
            <b>Status da Missão:</b> Concluída / Sucesso Parcial<br>
            <b>Descrição Básica:</b> Relatada flutuação gravitacional na ala de caldeiras e liquefação orgânica de matéria-prima. Uma equipe infiltrada localizou o foco paranormal. <span class="tarja-preta">OS AGENTES DETECTARAM QUE A ANOMALIA SE ALIMENTAVA DE</span>. Os funcionários sobreviventes receberam amnésicos de Classe C.
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

        st.write("") # Espaçamento entre blocos

        # --- LOG 2 ---
        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-05D</b></span><br>
            <b>Localização:</b> Campus Universitário [CONFIDENCIAL] - Ala de Anatomia Médica<br>
            <b>Status da Missão:</b> Arquivada / Contida<br>
            <b>Descrição Básica:</b> Um dos corpos fornecidos apresentou atividade muscular pós-morte espontânea e vocalização em frequências prejudiciais. Agentes do Grau AB agiram redirecionando estudantes. <span class="tarja-preta">O CADÁVER MANIFESTOU EXPANSÃO DE</span>. O espécime foi tratado conforme o Protocolo III.
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

        st.write("") # Espaçamento entre blocos

        # --- LOG 3 ---
        st.markdown("""
        <div class="bloco-confidencial">
            <span class="tag-vermelha"><b>ARQUIVO: EXP-2026-06B</b></span><br>
            <b>Localização:</b> Perímetro das Montanhas de Cinzas - Posto de Observação Avançado<br>
            <b>Status da Missão:</b> Ativa / Monitoramento Crítico<br>
            <b>Descrição Básica:</b> Detectado aumento na pressão atmosférica indicando movimentação de energia de espectro vermelho. Patrulhas de Caçadores foram posicionadas. <span class="tarja-preta">FOI VISUALIZADA UMA ESTRUTURA BIOLÓGICA DE CINZAS DE</span>. Risco iminente de exposição anômala.
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

    # --- DIRETÓRIO 6: TRANSMISSÃO CAIM ---
    elif opcao == "Transmissão C.A.I.M.":
        st.subheader("ARQUIVO DE INTERCEPTAÇÃO DE SINAL COMUNICATIVO")
        st.error("AVISO: Sinal corrompido por entidade externa não catalogada.")
        st.write("---")
        st.markdown("""
        > **Caim:** *Olá agente, espero que você esteja pronto para uma aventura que é de arrancar seu coração. Estarei nos cantos das páginas explicando sobre o sistema e dando algumas dicas. Eu serei uma figura bastante familiar durante ao decorrer do jogo então, se acostume... não é de todo mal receber minha ajuda, é um bom acordo...*
        """)