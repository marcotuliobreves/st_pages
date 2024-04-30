import streamlit as st
from st_pages import hide_pages
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

# add_page_title("PRO Carbono Commodities",layout="wide")

if st.button("⬅ VOLTAR"):
        switch_page("Commodities")

st.title("PRO Carbono Commodities")

# Tabela de grupos e talhões
st.subheader("Fazendas")


def action_button():
    if st.button("VER FAZENDA"):
        switch_page("Commodities Fazendas")

df = pd.DataFrame(
    {
        "farms": ['Fazenda Santa Terezinha', 'Vaca Branca'],
        "fields": ['7 Talhões', '41 Talhões',],
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
        "farms": "Fazendas",
        "fields": "Talhões",
        # "url": st.column_config.LinkColumn("App URL"),
        "action": "Ação"
    },
    hide_index=True
    # formatters={"action": action_button}
)

action_buttons = ["Ver Talhões"] * 3

if st.button("VER FAZENDA"):
    switch_page("Commodities Talhões")

# PS: Nessa página, além da conexão com o BD, está faltando implementar a lógica do botão de redirecionamento para a página
#     "Commodities Fazendas" em cada linha da tabela 