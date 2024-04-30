import streamlit as st
from st_pages import add_page_title, hide_pages

hide_pages(["Login","Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

add_page_title(layout="wide")

st.write("Este App foi desenvolvido como MVP para o projeto:")

st.write("**AUTOMATIZAÇÃO DOS DADOS DE INVENTÁRIO DO CONECTA**")

