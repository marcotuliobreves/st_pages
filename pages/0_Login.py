import streamlit as st
from st_pages import hide_pages
from streamlit_extras.switch_page_button import switch_page
import time

hide_pages(["Commodities Inventário Automatizado" ,"Login", "Início", "Fazendas", "PRO Carbono", "Commodities", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário","ADM Regeneração", "Benefícios", "Usuários", "Sair"])

st.title("MVP Automated Inventory Data")

username = st.text_input("Nome de usuário")
password = st.text_input("Senha", type="password")

if st.button("Login"):
    if username == "usuario" and password == "senha123**99":
        st.success("Login bem-sucedido")
        time.sleep(2)
        switch_page("Início")
    else:
        st.error("Nome de usuário ou senha incorretos")
