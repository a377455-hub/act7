import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5)
    
temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0)

if pH <= 6 or pH > 7:
    if temperatura <= 20 or temperatura >= 25:
        st.write("Revisar el pH")
    else:
        st.write("Revisar temperatura")
else: 
    st.write("Lote aceptable")

if st.button("Evaluar"):
    resultado: "Lote aceptable"
    st.write(f"Resultado: {resultado}")
