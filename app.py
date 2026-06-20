import numpy as np
import streamlit as st
import logica

st.title("Formulador Tortas Tres Leches")

torta_18000 = st.number_input("18.000", 0, 20, 0)
torta_25000 = st.number_input("25.000", 0, 20, 0)
torta_30000 = st.number_input("30.000", 0, 20, 0)
torta_40000 = st.number_input("40.000", 0, 20, 0)
torta_50000 = st.number_input("50.000", 0, 20, 0)
torta_75000 = st.number_input("75.000", 0, 20, 0)

tortas = [torta_18000, torta_25000, torta_30000, torta_40000, torta_50000, torta_75000]

batido_total = logica.calculo_batido(tortas)
jarabe_total = logica.calculo_jarabe(tortas)
col1, col2 = st.columns(2)

with col1:
    st.metric("Batido Total:", batido_total)

with col2:
    st.metric("Jarabe Total:", jarabe_total)

st.divider()

cantidad = logica.receta_batido(batido_total)
cantidad = [round(valor,0) for valor in cantidad]

batido_dict = {
    "ingredientes": ["huevos", "azucar", "harina pastelera", "polvo de hornear", "fecula", "sabor bizcocho"],
    "cantidad en gramos": cantidad
}
st.write("Receta Batido")
st.dataframe(batido_dict, use_container_width=True)

cantidad_jarabe = logica.receta_jarabe(jarabe_total)
cantidad_jarabe = [round(valor, 0) for valor in cantidad_jarabe]

jarabe_dict = {
    "ingredientes": ["leche liquida", "leche condensada", "leche en polvo", "azucar", "sabor tres leches"],
    "cantidad en gramos": cantidad_jarabe
}
st.divider()
st.write("Receta Jarabe")
st.dataframe(jarabe_dict, use_container_width=True)
