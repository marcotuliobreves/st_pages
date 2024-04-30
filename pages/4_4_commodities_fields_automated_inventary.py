import streamlit as st
from st_pages import hide_pages
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

hide_pages(["Login", "Commodities Fazendas", "Commodities Talhões", "Commodities Talhões Novo Inventário", "Commodities Inventário Automatizado"])

# add_page_title("PRO Carbono Commodities",layout="wide")
if st.button("⬅ VOLTAR"):
        switch_page("Commodities Talhões Novo Inventário")


st.title("Inventário de Dados Automatizado")

st.write("Valide os campos gerados automaticamente. Caso necessário, você pode editá-los.")

st.write("Preencha os campos que não foram gerados automaticamente.")

st.markdown("---")

st.subheader("Talhão VB1 - TH92") 

with st.expander("DADOS GERAIS"):
    responsible = st.text_input('Responsável pelo preenchimento*', 'Ricardo Durante Itacarambi')
    farm_name = st.text_input('Nome da Fazenda*', 'Vaca Branca')
    field_name = st.text_input('Nome do talhão*', 'VB1 - TH92')
    field_area = st.text_input('Área do talhão (ha)*', '92,7')
    harvestyear = st.text_input('Safra:','Verão 22/23')
    latitude = st.text_input('Latitude', '-9,543631')
    longitude = st.text_input('Longitude', '-56,279364')
    country = st.text_input('País', 'Brasil')
    state = st.text_input('Estado', 'MT')
    city = st.text_input('Município', 'Alta Floresta')

with st.expander("PRÉ-PLANTIO"):
    st.write("**Aplicação 1**")
    application1_date = st.text_input('Data da última aplicação', '23/10/2022')
    application1_frequency = st.text_input('Frequência de corretivo de solo aplicado', 'Anual')
    application1_type = st.text_input('Tipo de corretivo de solo aplicado', 'Calcário Calcítico')
    application1_quantity = st.text_input('Quantidade de corretivo de solo aplicado no talhão', '99')
    application1_uom = st.text_input('Unidade de medida', 'Kg/ha')
    application1_qtt_cultures = st.text_input('Quantas culturas comerciais no ano safra desse talhão', '2')
    st.button("**ADICIONAR NOVA APLICAÇÃO**")

with st.expander("PLANTIO"):
    culture = st.text_input('Cultura', 'Soja')
    st.write("**OPERAÇÃO 1**")
    planting1_operation_type = st.text_input('Tipo de operação', 'Plantio')
    planting1_genetics = st.text_input('Genética', 'Dado médio de todas as genéticas')
    planting1_area_ha = st.text_input('Área plantada (ha)', '89')
    planting1_seeds = st.text_input('Sementes aplicadas', '3,6')
    planting1_seeds_uom = st.text_input('Unidade de medida', 'nº de sementes/m')
    planting1_pms = st.text_input('Peso de mil sementes (PMS) em gramas', '333')
    planting1_distance = st.text_input('Distância entre as linhas de plantio (cm)', '55')
    planting1_date = st.text_input('Data do plantio', '11/01/2023')
    planting1_obs = st.text_input('Observações Gerais', '')
    st.button("**ADICIONAR NOVA OPERAÇÃO**")

with st.expander("MANEJO"):
     st.subheader("Fertilizantes de solo aplicados no talhão")
     st.write("**APLICAÇÃO 1**")
     fertilizer_1 = st.text_input('Fertilizante Aplicação 1', 'Cloreto de potássio')
     fertilizer_quantity_1 = st.text_input('Quantidade de fertilizante Aplicação 1', '56,5 kg/ha')
     st.write("**APLICAÇÃO 2**")
     fertilizer_2 = st.text_input('Fertilizante Aplicação 2', 'Fosfato monoamônico (MAP)')
     fertilizer_quantity_2 = st.text_input('Quantidade de fertilizante Aplicação 2', '162,56 kg/ha')
     st.button("**NOVA APLICAÇÃO FERTILIZANTE**")

     st.markdown("---")

     st.subheader("Máquinas agrícolas")
     st.write("**COMBUSTÍVEL 1**")
     fuel_1 = st.text_input('Combustível utilizado 1', 'Diesel')
     fuel_quantity_1 = st.text_input('Quantidade de combustível utilizado 1', '44,5 L/ha')
     st.button("**NOVO COMBUSTÍVEL**")
     
with st.expander("COLHEITA"):
    harvest_date = st.text_input('Data final de colheita', '22/03/2023')
    harvest_yield = st.text_input('Produtividade', '90,69')
    harvest_uom = st.text_input('Unidade de medida', 'scs/ha')
    harvest_moisture = st.text_input('Umidade do grão colhido (%)', '15,67')
    harvest_burning_waste= st.text_input('Houve queima de resíduos agrícolas por manejo ou fogo acidental', 'Não')

with st.expander("ENERGIA"):
    st.subheader("Origem das fontes de energia elétrica que alimentam a fazenda:")
    grid = st.text_input('Grid', '0 %')
    grid = st.text_input('Pequena Central Hidroelétrica (PCH)', '100 %')
    grid = st.text_input('Gerador a diesel', '0 %')
    grid = st.text_input('Fotovoltaica', '0 %')

    st.markdown("---")

    st.subheader("Irrigação")
    irrigation = st.selectbox('Houve irrigação?',['Não','Sim'])
    if irrigation == 'Sim':
        irrigation_quantity = st.text_input('Quantidade de energia elétrica utilizada na irrigação (kWh/ha)', '')

    st.markdown("---")

    st.subheader("Secagem de grãos")
    grain_drying = st.selectbox('Houve secagem dos grãos dentro da propriedade?',['Não','Sim'])
    if grain_drying == 'Sim':
        gran_drying_volume = st.text_input('Volume de grãos desse talhão que passou por secagem (%)', '80')
        gran_drying_sugarcane = st.text_input('Secagem utilizando bagaço de cana como combustível (%)', '')
        gran_drying_cavaco = st.text_input('Secagem utilizando cavaco como combustível (%)', '95')
        gran_drying_glp = st.text_input('Secagem utilizando GLP de cana como combustível (%)', '')
        gran_drying_native_wood = st.text_input('Secagem utilizando lenha de madeira nativa como combustível (%)', '')
        gran_drying_planted_wood = st.text_input('Secagem utilizando lenha de madeira plantada como combustível (%)', '')
        gran_drying_fuel_oil = st.text_input('Secagem utilizando óleo combustível como combustível (%)', '')
        gran_drying_electricity = st.text_input('Secagem utilizando energia/eletricidade como combustível (%)', '5')
        gran_drying_other_biomass = st.text_input('Secagem utilizando outro combustível de biomassa (%)', '')

with st.expander("TRANSPORTE"):
     weight = st.text_input('Peso da cultura transportada', '484,28 ton')
     modal = st.text_input('Modal de transporte da soja no percurso da fazenda-trader', 'Rodoviário')
     distance_trader = st.text_input('Distância percorrida no trecho fazenda-trader', '978,52 km')
     moisture_transport = st.text_input('Umidade do grão na expedição', '14,00 %')
     st.button("**INCLUIR MODAL**")

st.markdown("---")

with stylable_container(
    "green",
    css_styles="""
    button {
        background-color: #00FF00;
        color: black;
    }""",
):
    buttongreen_clicked = st.button("FINALIZAR", key="buttongreen")

if buttongreen_clicked:
      switch_page("Commodities Talhões")