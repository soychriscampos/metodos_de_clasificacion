import pandas as pd
import numpy as np
import statsmodels.api as sm

dataframe = pd.read_csv('calificaciones.csv')

# Declaración de variables independientes y dependientes
x = dataframe[['calificacion_examen', 'clases_perdidas']]
y = dataframe['calificacion_estadistica']

# Estimación de la Matriz
# -- Se añade columna de unos -intersección- (bias)
x = sm.add_constant(x)
# -- Cálculo de la matriz
modelo = sm.OLS(y, x).fit()
# print(modelo.params)

# Estimando calificación de estadística: examen = 60 clases perdidas = 4
nuevo_estudiante = pd.DataFrame({
    'const': [1],
    'calificacion_examen': [60],
    'calses_perdidas': [4]
})
# -- Predecir la calificación (+ conversión a valor escalar)
prediccion = modelo.predict(nuevo_estudiante).iloc[0]


# Cálculo de los datos de la tabla solicitada
# -- valores de y_gorro
dataframe['y_prediccion'] = modelo.predict(x)
# -- e
dataframe['e'] = dataframe['calificacion_estadistica'] - \
    dataframe['y_prediccion']
# -- SCE
dataframe['SCE'] = dataframe['e'] ** 2
sce = dataframe['SCE'].sum()

# Cálculo del error estándar de la estimación múltiple
# -- No. de observaciones
n = len(dataframe)
# -- No. de variables independientes (-1 para no incluir columna de unos)
k = x.shape[1] - 1
# -- error estándar
error_estandar = np.sqrt(sce / (n - k - 1))

# Cálculo de SCR y STC
# -- media de la variable dependiente
y_media = y.mean()
# -- SCR
dataframe['SCR'] = (dataframe['y_prediccion'] - y_media) ** 2
scr = dataframe['SCR'].sum()
# -- STC
stc = sce + scr

# Cálculo del coeficiente de determinación múltiple (r^2)
r2 = scr / stc
r2 = round(r2*100, 2)

# Resultados solicitados
print("La calificación estimada del estudiante será:", round(prediccion))
print("\n --- CÁLCULOS EN LA TABLA ---- ")
print(dataframe.to_string(index=False))
print("La suma de cuadrados del error es:", sce)
print("\nEl error de la estimación estándar múltiple es:", error_estandar)
print("\n --- CÁLCULOS EN LA TABLA con SCR---- ")
print(dataframe.to_string(index=False))
print("La suma de cuadrados del error (SCE) es:", sce)
print("La suma de cuadrados de la regresión (SCR) es:", scr)
print("La suma total de cuadrados (STC) es:", stc)
print("\nCoeficiente de determinación múltiple(r^2) es: ", r2, "%")
