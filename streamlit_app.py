import streamlit as st
import pandas as pd

st.title("Sustancias Relacionadas")


st.write(
    "Seleccionar archivos en formato CSV"
)

uploaded_file = st.file_uploader("Blanco:")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe_blanco = pd.read_csv(uploaded_file,sep=',')
    st.write(dataframe_blanco)

uploaded_file = st.file_uploader("Muestra:")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe_muestra = pd.read_csv(uploaded_file,sep=',')
    st.write(dataframe_muestra)

intervalo_por = st.number_input("Insertar intervalo de tiempo(%): ")
area_multp = st.number_input("Insertar multiplicador área: ")