import streamlit as st
import io
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Algoritmo de Regresión Lineal")

    # Aquí va el código para cargar los datos
 archivo_csv = "registro.csv"  
    datos_sec = pd.read_csv(archivo_csv, encoding='latin-1', on_bad_lines='skip')
        st.write("Datos cargados:")
        st.write(datos_sec)

        # Realiza las visualizaciones de datos y gráficos
        st.write("Podemos visualizar datos específicos:")
        st.write(datos_sec["DEPARTAMENTO"])

        st.write("Información de los datos cargados:")
        st.write(datos_sec.info())

        st.write("Histogramas para la visualización de los datos:")
        st.write(datos_sec.hist())

        st.write("Nueva tabla con solo los datos relevantes para el objetivo:")
        st.write(datos_sec)

        st.write("Grafico de dispersión (FEMENINO Vs CANT. DE PARTICIPANTES):")
        plt.scatter(x=datos_sec['FEMENINO'], y=datos_sec['CANT. DE PARTICIPANTES'])
        plt.title('FEMENINO Vs CANT. DE PARTICIPANTES')
        plt.xlabel('FEMENINO')
        plt.ylabel('CANT. DE PARTICIPANTES')
        st.pyplot()

        st.write("Grafico de dispersión (MASCULINO Vs CANT. DE PARTICIPANTES):")
        plt.scatter(x=datos_sec['MASCULINO'], y=datos_sec['CANT. DE PARTICIPANTES'])
        plt.title('MASCULINO Vs CANT. DE PARTICIPANTES')
        plt.xlabel('MASCULINO')
        plt.ylabel('CANT. DE PARTICIPANTES')
        st.pyplot()

if __name__ == "__main__":
    main()
