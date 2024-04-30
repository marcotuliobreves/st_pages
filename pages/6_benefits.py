import streamlit as st
from st_pages import add_page_title, hide_pages

hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

add_page_title(layout="wide")

st.write("Nesta página do Conecta, são exibidas as parcerias e benefícios exclusivos PRO Carbono.")

st.write("Para este MVP, essa tela é apenas demonstrativa.")
