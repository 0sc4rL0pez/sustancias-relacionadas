import streamlit as st
import pandas as pd

st.title("Sustancias Relacionadas")
st.subheader("Modo de uso:")
st.write("Tanto para el blanco como para la muestra, hacer click derecho en la tabla de integración en el post run y seleccionar *Copy Entire Table*")
st.write("Crear un nuevo excel y pegar la tabla, exportar los datos en formato archivo .csv: ")
st.write("Archivo --> Exportar --> Cambiar el tipo de archivo --> CSV (delimitado por comas)")
st.write("Subir dicho archivo a su lugar correspondiente (Revisar que el estilo de la tabla sea el mismo en cada archivo")
st.write("Descargar el resultado")
st.subheader("Identificacion de picos a partir de un blanco")
st.write(
    "Seleccionar archivos en formato .CSV"
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

        intervalo_tiempo = st.number_input("Insertar intervalo de tiempo: ",value=0.25)
        area_multp = st.number_input("Insertar multiplicador área: ",value=2)
        columnas = dataframe_muestra.columns.tolist()
        col_time= columnas.index("Ret. Time")
        col_area = columnas.index("Area")
        dataframe_muestra['Name'] = ""
        #dataframe_muestra['Var Time'] = np.inf
        

        def estaEntiempo(t,j):
            ultima_area = -1
            ultima_fila_muestra = 0
            for i,val in enumerate(dataframe_muestra.iloc[:,col_time].tolist()):
                val = float(val)
                #var_time = abs(100*(val-t))/t
                var_time = abs(val-t)
                if var_time<intervalo_tiempo:
                    area_blanco = float(dataframe_blanco.iloc[j,col_area])
                    area_muestra = float(dataframe_muestra.iloc[i,col_area])
                    if area_blanco*2 >= area_muestra:
                        if (ultima_area == -1):
                            dataframe_muestra.loc[i,"Name"] = "Blanco"
                            ultima_area = area_muestra
                            ultima_fila_muestra = i
                        elif (ultima_area<area_muestra):
                                dataframe_muestra.loc[i,"Name"] = "Blanco"
                                ultima_area = area_muestra
                                ultima_fila_muestra = i
                                dataframe_muestra.loc[ultima_fila_muestra,"Name"] = ""


            
        
        for j,val in enumerate(dataframe_blanco.iloc[:,col_time].tolist()):
            estaEntiempo(float(val),j)

        st.write(dataframe_muestra)

        st.download_button(
            "Descargar archivo",
            dataframe_muestra.to_csv(index=False).encode('utf-8'),
            "file.csv",
            "text/csv",
            )

st.subheader("Ejemplos")

dataframe_bco = pd.read_csv("blanco.csv")
st.download_button(
            "Descargar blanco",
            dataframe_bco.to_csv(index=False).encode('utf-8'),
            "file.csv",
            "text/csv",
            )
dataframe_muestr = pd.read_csv("muestra.csv")
st.download_button(
            "Descargar muestra",
            dataframe_muestr.to_csv(index=False).encode('utf-8'),
            "file.csv",
            "text/csv",
            )
