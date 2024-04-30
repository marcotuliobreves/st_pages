import streamlit as st
import pandas as pd

# Defina uma chave para o estado da sessão
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Função para mudar a página e reexecutar o script
def go_to_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# Página Login
def login():
    st.title("MVP Automated Inventory Data")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if username == "usuario" and password == "senha123**99":
            st.success("Login bem-sucedido")
            go_to_page('commodities')
        else:
            st.error("Nome de usuário ou senha incorretos")

# Página Commodities
def commodities():
    st.title("PRO Carbono Commodities")

    # # Adicionando um sidebar para navegação
    # st.sidebar.info("Início")
    # st.sidebar.info("Fazendas")
    # st.sidebar.info("Programas")
    # st.sidebar.markdown("---")
    # st.sidebar.title("Programas")
    # # Destacando a seção "Commodities"
    # st.sidebar.info("PRO Carbono")
    # st.sidebar.markdown('<style>div.Widget.row-widget.stRadio > div{background-color: #ffffff}</style>', unsafe_allow_html=True)
    # st.sidebar.info("Commodities")
    # st.sidebar.info("Soluções")
    # st.sidebar.info("ADM regeneração")
    # st.sidebar.markdown("---")
    # st.sidebar.info("Benefícios")
    # st.sidebar.info("Usuários")
    # st.sidebar.info("Sair")

    # Adicionando um sidebar para navegação
    st.sidebar.info("Início")
    st.sidebar.info("Fazendas")
    st.sidebar.info("Programas")
    st.sidebar.markdown("---")
    st.sidebar.title("Programas")
    st.sidebar.info("PRO Carbono")
    with st.sidebar.container():
        st.info("Commodities")
    st.sidebar.info("Soluções")
    st.sidebar.info("ADM regeneração")
    st.sidebar.markdown("---")
    st.sidebar.info("Benefícios")
    st.sidebar.info("Usuários")
    st.sidebar.info("Sair")


    # Tabela de grupos e talhões
    st.subheader("Grupos e Talhões Cadastrados")
    # Exemplo de tabela com grupos, talhões cadastrados e botão "Ver Grupo"
    data = {
        'Grupo': ['Scheffer', 'Bom futuro', 'Natter'],
        'Talhões cadastrados': ['23 Talhões', '101 Talhões', '2 Talhões'],
        'EMC': ['Abraão', 'Alex Augusto', 'Alisson']
    }
    df = pd.DataFrame(data)
    st.table(df)
    for grupo in data['Grupo']:
        if st.button(f"Ver {grupo}"):
            # Lógica para visualizar o grupo selecionado
            st.write(f"Visualizando o grupo {grupo}")

# Lógica para alternar entre páginas
if st.session_state.page == 'login':
    login()
elif st.session_state.page == 'commodities':
    commodities()