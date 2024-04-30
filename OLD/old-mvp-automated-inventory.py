import streamlit as st
import pandas as pd
import random

# Defina uma chave para o estado da sessão
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Função para mudar a página e reexecutar o script
def go_to_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# # Função para criar a entrada de sidebar com destaque
# def sidebar_link(text, page_name, current_page):
#     # Se for a página atual, destaque
#     if page_name == current_page:
#          st.sidebar.button(text)
#     else:
#          st.sidebar.button(text, on_click=lambda: go_to_page(page_name))

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

    # Adicionando um sidebar para navegação
    st.sidebar.button("Início")
    st.sidebar.button("Fazendas")
    st.sidebar.button("Programas")
    st.sidebar.markdown("---")
    st.sidebar.title("Programas")
    st.sidebar.button("PRO Carbono")
    st.sidebar.button("Commodities")
    st.sidebar.button("Soluções")
    st.sidebar.button("ADM regeneração")
    st.sidebar.markdown("---")
    st.sidebar.button("Benefícios")
    st.sidebar.button("Usuários")
    st.sidebar.button("Sair", on_click=lambda: go_to_page('login'))

    # Tabela de grupos e talhões
    st.subheader("Grupos e Talhões Cadastrados")
    # Exemplo de tabela com grupos, talhões cadastrados e botão "Ver Grupo"
    # data = {
    #     'Grupo': ['Scheffer', 'Bom futuro', 'Natter'],
    #     'Talhões cadastrados': ['23 Talhões', '101 Talhões', '2 Talhões'],
    #     'EMC': ['Abraão', 'Alex Augusto', 'Alisson']
    # }
    # df = pd.DataFrame(data)
    # st.table(df)
    # for grupo in data['Grupo']:
    #     if st.button(f"Ver {grupo}"):
    #         # Lógica para visualizar o grupo selecionado
    #         st.write(f"Visualizando o grupo {grupo}")
    
    df = pd.DataFrame(
        {
            "group": ['Scheffer', 'Bom futuro', 'Natter'],
            "fields": ['23 Talhões', '101 Talhões', '2 Talhões'],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "action": st.page_link('login', label=None, icon=None, help=None, disabled=False, use_container_width=None)
        }
    )
    st.dataframe(
        df,
        column_config={
            "group": "Grupo",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "fields": "Talhões Cadastrados",
            "action": "Action",
        },
        hide_index=True,
    )


# Lógica para alternar entre páginas
if st.session_state.page == 'login':
    login()
elif st.session_state.page == 'commodities':
    commodities()