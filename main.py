
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def scatter_plot(datos, x_col, y_col, title, x_label, y_label):
    plt.scatter(x=datos[x_col], y=datos[y_col])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot()

def main():
  import matplotlib.pyplot as plt
plt.scatter(x=datos_sec['FEMENINO'], y=datos_sec['CANT. DE PARTICIPANTES'])
plt.title('FEMENINO Vs CANT. DE PARTICIPANTES')
plt.xlabel('FEMENINO')
plt.ylabel('CANT. DE PARTICIPANTES')
plt.show()

import matplotlib.pyplot as plt
plt.scatter(x=datos_sec['MASCULINO'], y=datos_sec['CANT. DE PARTICIPANTES'])
plt.title('MASCULINO Vs CANT. DE PARTICIPANTES')
plt.xlabel('MASCULINO')
plt.ylabel('CANT. DE PARTICIPANTES')
plt.show()

    scatter_plot(datos_sec, 'FEMENINO', 'CANT. DE PARTICIPANTES', 'FEMENINO Vs CANT. DE PARTICIPANTES', 'FEMENINO', 'CANT. DE PARTICIPANTES')
    scatter_plot(datos_sec, 'MASCULINO', 'CANT. DE PARTICIPANTES', 'MASCULINO Vs CANT. DE PARTICIPANTES', 'MASCULINO', 'CANT. DE PARTICIPANTES')

    st.write("Esta es la nueva tabla con solo los datos relevantes para el objetivo")
    st.write(datos_sec)

    st.write("# **FASE 2. Entrenamiento del modelo**")
"""# **FASE 2. Entrenamiento del modelo**

Aqui separamos los datos en 2 partes, el primero en datos de entrenamiento  el cual seran un 80% de la informacion de la tabla y el segundo seran los datos de test que corresponden a un 20%.
"""

datos_entrenamiento = datos_sec.sample(frac=0.8, random_state=0)
datos_test = datos_sec.drop(datos_entrenamiento.index)

    st.write(datos_entrenamiento)
    st.write(datos_test)


"""Aqui se quitaran la columna con los datos a predecir(cant. de participantes) a las dos tablas nuevas creadas(datos_entrenamiento y datos_test)"""

etiquetas_entrenamiento = datos_entrenamiento.pop('CANT. DE PARTICIPANTES')
etiquetas_test = datos_test.pop('CANT. DE PARTICIPANTES')
    st.write(datos_entrenamiento)
    st.write(datos_test)

    st.write("# **FASE 3. Predicciones**")
"""# **FASE 3. Predicciones**

Se utilizara la regresion lineal para empezar las predicciones
"""

from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(datos_entrenamiento,etiquetas_entrenamiento)

predicciones = modelo.predict(datos_test)
    st.write(predicciones)

    st.write("Aqui calculamos el margen de error en la prediccion de la CANT. DE PARTICIPANTES.")
import numpy as np
from sklearn.metrics import mean_squared_error
error = np.sqrt(mean_squared_error(etiquetas_test, predicciones))

    st.write("Error porcentual:", error*100)

if __name__ == "__main__":
    main()
