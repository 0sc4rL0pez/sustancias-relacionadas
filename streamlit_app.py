import streamlit as st

st.title("Sustancias Relacionadas")
st.write(
    "App para realizar la identificacion de picos en cromatogramas"
)

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    st.write('\n')