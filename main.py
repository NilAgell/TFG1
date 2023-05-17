import streamlit as st
import numpy as np

def vector_calculator():
    st.title("Calculadora de Vectores")

    # Pedir la dimensión del vector 1
    dim1 = st.number_input("Ingrese la dimensión del vector 1:", min_value=1, step=1, value=2)

    # Pedir los valores del vector 1
    st.write("Ingrese los valores del vector 1:")
    vector1 = []
    for i in range(dim1):
        value = st.number_input(f"Valor {i+1}:", key=f"vector1_{i}")
        vector1.append(value)

    # Pedir la dimensión del vector 2
    dim2 = st.number_input("Ingrese la dimensión del vector 2:", min_value=1, step=1, value=2)

    # Pedir los valores del vector 2
    st.write("Ingrese los valores del vector 2:")
    vector2 = []
    for i in range(dim2):
        value = st.number_input(f"Valor {i+1}:", key=f"vector2_{i}")
        vector2.append(value)

    # Mostrar los vectores ingresados
    st.write("Vector 1:", vector1)
    st.write("Vector 2:", vector2)

    # Verificar si se seleccionó sumar o restar
    operation = st.radio("Seleccione una operación:", ("Sumar", "Restar"))

    # Calcular la suma o resta de los vectores
    result = []
    if operation == "Sumar":
        if dim1 == dim2:
            result = np.add(vector1, vector2)
        else:
            st.error("Las dimensiones de los vectores no coinciden.")
    else:
        if dim1 == dim2:
            result = np.subtract(vector1, vector2)
        else:
            st.error("Las dimensiones de los vectores no coinciden.")

    # Mostrar el resultado
    st.write("Resultado:", result)


if __name__ == "__main__":
    vector_calculator()
