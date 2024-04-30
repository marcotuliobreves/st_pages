import streamlit as st
from streamlit.components.v1 import html

def main():
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

    # Recebendo e processando os parâmetros de consulta
    params = st.experimental_get_query_params()
    if "next" in params and params["next"] == ["commodities"]:
        # Exibindo a página de commodities
        st.write("Conteúdo da página de commodities")

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

if __name__ == "__main__":
    main()