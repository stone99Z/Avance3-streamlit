# -*- coding: utf-8 -*-
"""Avance3.ipynb

# **ALGORITMO DE REGRESION LINEAL**

Objetivo: Prediccion de datos.

# **FASE 1. Preparacion de datos**
"""

from google.colab import files
uploaded = files.upload()

"""Se carga la libreria de pandas"""

import io
import pandas as pd
datos_sec = pd.read_csv(io.BytesIO(uploaded['registro.csv']),encoding='latin-1', on_bad_lines='skip')

"""Visualizamos los datos cargados"""

datos_sec

"""Podemos visualizar datos especificos"""

datos_sec["DEPARTAMENTO"]

"""Nos brinda informacion de los datos cargados, como el tipo de los datos, la cantidad de datos(643 datos), etc."""

datos_sec.info()

"""Se hicieron histogramas para la visualiacion de los datos"""

datos_sec.hist()

datos_sec

"""Aqui podremos saber cuantos datos no exitentes o espacios vacios hay por columna"""

datos_sec.isna().sum()

"""Luego empezamos a quitar los datos(columnas) que no aportan al objetivo principal(predecir la cant. de participantes)"""

datos_sec = datos_sec.drop(columns=['CENTRO POBLADO'])
datos_sec = datos_sec.drop(columns=['COMUNIDAD CAMPESINA O NATIVA'])
datos_sec = datos_sec.drop(columns=['DEPARTAMENTO'])
datos_sec = datos_sec.drop(columns=['NOMBRE DEL EVENTO'])

datos_sec

datos_sec = datos_sec.drop(columns=['TRIMESTRE'])
datos_sec

datos_sec = datos_sec.drop(columns=['PROVINCIA'])
datos_sec

datos_sec = datos_sec.drop(columns=['DISTRITO'])
datos_sec

"""Se realizaron graficos de dispersion"""

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

"""Esta es la nueva tabla con solo los datos relevantes para el objetivo"""

datos_sec

"""# **FASE 2. Entrenamiento del modelo**

Aqui separamos los datos en 2 partes, el primero en datos de entrenamiento  el cual seran un 80% de la informacion de la tabla y el segundo seran los datos de test que corresponden a un 20%.
"""

datos_entrenamiento = datos_sec.sample(frac=0.8, random_state=0)
datos_test = datos_sec.drop(datos_entrenamiento.index)

datos_entrenamiento

datos_test

"""Aqui se quitaran la columna con los datos a predecir(cant. de participantes) a las dos tablas nuevas creadas(datos_entrenamiento y datos_test)"""

etiquetas_entrenamiento = datos_entrenamiento.pop('CANT. DE PARTICIPANTES')
etiquetas_test = datos_test.pop('CANT. DE PARTICIPANTES')

datos_entrenamiento

datos_test

"""# **FASE 3. Predicciones**

Se utilizara la regresion lineal para empezar las predicciones
"""

from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(datos_entrenamiento,etiquetas_entrenamiento)

predicciones = modelo.predict(datos_test)
predicciones

"""Aqui calculamos el margen de error en la prediccion de la CANT. DE PARTICIPANTES."""

import numpy as np
from sklearn.metrics import mean_squared_error
error = np.sqrt(mean_squared_error(etiquetas_test, predicciones))
print("Error porcentual : %f" % (error*100))
