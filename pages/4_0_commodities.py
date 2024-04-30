import streamlit as st
from st_pages import hide_pages
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

st.title("PRO Carbono Commodities")

# Tabela de grupos e talhões
st.subheader("Grupos e Talhões Cadastrados")

def action_button():
    if st.button("VER FAZENDA"):
        switch_page("Commodities Fazendas")

df = pd.DataFrame(
    {
        "group": ['Scheffer', 'Bom Futuro', 'Natter'],
        "fields": ['23 Talhões', '101 Talhões', '5 Talhões'],
        # "url": ["http://localhost:8501/Commodities%20Fazendas", "http://localhost:8501/Commodities%20Fazendas", "http://localhost:8501/Commodities%20Fazendas"]
        "action": action_button
        # "action": action_buttons
        # "action": st.page_link('app.py', label=None, icon=None, help=None, disabled=False, use_container_width=None)
        # "action": st.page_link('fields', label=None, icon=None, help=None, disabled=False, use_container_width=None)
    }
)

st.dataframe(
    df,
    column_config={
        "group": "Grupo",
        "fields": "Talhões Cadastrados",
        # "url": st.column_config.LinkColumn(label='Ação', width=None, help=None, disabled=None, required=None, default=None, max_chars=None, validate=None, display_text='Ver Grupo')
        "action": "Ação"
    },
    hide_index=True
    # formatters={"action": action_button}
)

action_buttons = ["Ver Talhões"] * 3

if st.button("VER GRUPO"):
    switch_page("Commodities Fazendas")

# PS: Nessa página, além da conexão com o BD, está faltando implementar a lógica do botão de redirecionamento para a página
#     "Commodities Fazendas" em cada linha da tabela 