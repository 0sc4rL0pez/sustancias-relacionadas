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

        intervalo_tiempo = st.number_input("Insertar intervalo de tiempo(%): ",value=0.5)
        area_multp = st.number_input("Insertar multiplicador área: ",value=2)
        col_time= int(st.number_input("Nro columna para tiempo ret"))
        col_area = int(st.number_input("Nro columna para area"))

        def estaEntiempo(t):
            for val in dataframe_muestra.iloc[:,col_time].tolist():
                if abs(100*(val-t)/t<intervalo_tiempo):
                    return True
            
            return True
        dataframe_blanco['esta'] = dataframe_blanco.iloc[:,col_time].map(lambda x:estaEntiempo(x))

        st.write(dataframe_blanco['esta'])