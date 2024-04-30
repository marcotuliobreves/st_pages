import streamlit as st
from st_pages import hide_pages
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

# add_page_title("PRO Carbono Commodities",layout="wide")
if st.button("⬅ VOLTAR"):
        switch_page("Commodities Talhões")


st.title("PRO Carbono Commodities")

st.write("Safra:")
st.code("Verão 22/23")

st.write("Cultura:")
st.code("Soja")

# Tabela de grupos e talhões
st.subheader("Fazenda Santa Terezinha") 

st.markdown("---")

st.subheader("Selecione os talhões que deseja importar e realizar o inventário:")

data_df = pd.DataFrame(
    {
        "Talhões": ["VB1 - TH92", "VB1 - TH140", "VB2 - TH176", "VB4 - TH75"],
        "Check": [False, False, False, False],
    }
)

st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            help="Selecione os **talhões** para o inventário",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
)

with stylable_container(
    "green",
    css_styles="""
    button {
        background-color: #00FF00;
        color: black;
    }""",
):
    buttongreen_clicked = st.button("**GERAR INVENTÁRIO AUTOMATIZADO**", key="buttongreen")

if buttongreen_clicked:
      switch_page("Commodities Inventário Automatizado")