import streamlit as st

def pagina_inicial():
    st.title('Página Inicial')
    if st.button('Ir para outra página'):
        st.markdown('<meta http-equiv="refresh" content="0;URL=http://localhost:8501">', unsafe_allow_html=True)

def outra_pagina():
    st.title('Outra Página')
    st.write('Você foi redirecionado para outra página!')

pagina_inicial()