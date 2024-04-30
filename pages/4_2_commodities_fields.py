import streamlit as st
from st_pages import hide_pages
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

# add_page_title("PRO Carbono Commodities",layout="wide")
if st.button("⬅ VOLTAR"):
        switch_page("Commodities Fazendas")


st.title("PRO Carbono Commodities")

# Tabela de grupos e talhões
st.subheader("Fazenda Santa Terezinha") 

with st.popover("**ADICIONAR INVENTÁRIO**"):
    st.markdown("Selecione o ano-safra e a cultura. Você poderá alterar essa informação depois.")
    safra = st.selectbox(
    'Selecione a safra:',
    ('Verão 22/23','Verão 23/24','Verão 24/25','Verão 25/26','Verão 26/27','Verão 27/28','Verão 28/29','Verão 29/30','Inverno 23/23','Inverno 24/24','Inverno 25/25','Inverno 26/26','Inverno 27/27','Inverno 28/28','Inverno 29/29','Inverno 30/30','Safrinha (Outono) 23/23','Safrinha (Outono) 24/24','Safrinha (Outono) 25/25','Safrinha (Outono) 26/26','Safrinha (Outono) 27/27','Safrinha (Outono) 28/28','Safrinha (Outono) 29/29','Safrinha (Outono) 30/30'))
    safra = st.selectbox(
    'Selecione a cultura:',
    ('Soja','Milho'))
    if st.button("CONTINUAR"):
        switch_page("Commodities Talhões Novo Inventário")

st.markdown("---")

st.subheader("Inventários Realizados")

def action_button():
    if st.button("VER FAZENDA"):
        switch_page("Commodities Fazendas")

df = pd.DataFrame(
    {
        "harvestyear": ['Safra Inverno 23/23', 'Safra Verão 22/23'],
        "culture": ['Milho', 'Soja'],
        "fields": ['2 Talhões', '1 Talhões',],
        # "url": ["http://localhost:8501/Commodities%20Fazendas", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "action": action_button
        # "action": action_buttons
        # "action": st.page_link('app.py', label=None, icon=None, help=None, disabled=False, use_container_width=None)
        # "action": st.page_link('fields', label=None, icon=None, help=None, disabled=False, use_container_width=None)
    }
)

st.dataframe(
    df,
    column_config={
        "harvestyear": "Safra",
        "culture": "Cultura",
        # "url": st.column_config.LinkColumn("App URL"),
        "fields": "Talhões",
        "action": "Ação"
    },
    hide_index=True
    # formatters={"action": action_button}
)

st.button("VER TALHÕES")


action_buttons = ["Ver Talhões"] * 3


# PS: Nessa página, além da conexão com o BD, está faltando implementar a lógica do botão de redirecionamento para a página
#     "Commodities Fazendas" em cada linha da tabela 