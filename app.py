import streamlit as st

st.title("Evaluación de un lote")

st.sidebar.title("Sarah Peña")
st.sidebar.title("Programación")
st.sidebar.title("Facultad de Ciencias Químicas")

pH = st.number_input(
    "pH",
    value=6.5)
    
temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0)

if pH >= 6 and pH < 7:
    st.write("pH adecuado")
    
    if temperatura >= 20 and temperatura <= 25:
        st.write("Lote aceptable")
        
    else:
        st.write("Revisar temperatura")
else:
    st.write("Revisar el pH")

#if st.button("Evaluar"):
    #resultado = "Lote aceptable"
    #st.write(f"Resultado: {resultado}")
