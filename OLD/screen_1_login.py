import streamlit as st

def login():
    st.title("MVP Automated Inventory Data")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if username == "usuario" and password == "senha123":
            st.success("Login bem-sucedido")
            commodities()
        else:
            st.error("Nome de usuário ou senha incorretos")


def commodities():
    st.title("PRO Carbono Commodities")

    # Adicionando um sidebar para navegação
    st.sidebar.info("Início")
    st.sidebar.info("Fazendas")
    st.sidebar.info("Programas")
    st.sidebar.markdown("---")
    st.sidebar.title("Programas")
    st.sidebar.info("PRO Carbono")
    st.sidebar.info("Commodities")
    st.sidebar.info("Soluções")
    st.sidebar.info("ADM regeneração")
    st.sidebar.markdown("---")
    st.sidebar.info("Benefícios")
    st.sidebar.info("Usuários")
    st.sidebar.info("Sair")

    # Listando grupos e talhões
    st.subheader("Grupos e Talhões Cadastrados")
    # Exemplo de listagem de grupos e talhões
    st.markdown("""
    - Grupo EMC
        - Abraão EMC, Alex Augusto (BIP), Alisson, Ana Líndiner Lima de Araújo (BIP), TesteEMC...
    - Grupo Bom futuro
        - 101 Talhões...
    - Grupo Família Silva
        - 2 Talhões...
    - Grupo Gelati
        - 68 Talhões...
    - Grupo Heloisa
        - Alisson, Ana Líndiner Lima de Araújo (BIP), Michelle EMC, Teste EMC...
    - Grupo SAFE TRACE
        - 7 Talhões...
    - Grupo Verde
        - 1 Talhão...
    - NovoH
        - 2 Talhões...
    - Priscila J
        - 18 Talhões...
    """)

login()