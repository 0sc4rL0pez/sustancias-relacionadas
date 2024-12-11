import streamlit as st
import pandas as pd
import numpy as np
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
        col_time= int(st.number_input("Nro columna para tiempo ret",value=1))
        col_area = int(st.number_input("Nro columna para area",value=2))
        dataframe_muestra['Pico_presente'] = False
        dataframe_muestra['Var Time'] = np.inf
        def areaCorrecta(fila):
            return float(dataframe_blanco.iloc[fila,col_area])*2 >= float(dataframe_muestra.iloc[fila,col_area])

        def estaEntiempo(t):
            contador = 0
            for val in dataframe_muestra.iloc[:,col_time].tolist():
                val = float(val)
                var_time = abs(100*(val-t))/t
                if var_time<intervalo_tiempo:
                    dataframe_muestra.loc[contador,"Var Time"] = min(var_time, dataframe_muestra["Var Time"][contador])
                    if areaCorrecta(contador):
                        dataframe_muestra.loc[contador,"Pico_presente"] = True
                contador = contador + 1
            
        for val in dataframe_blanco.iloc[:,col_time].tolist():
            estaEntiempo(float(val))

        st.write(dataframe_muestra)