import pandas as pd
import matplotlib.pyplot as plt

# importación de datos
dataframe = pd.read_csv("remodelaciones.csv")

# Creación del diagrama de disperción.
plt.scatter(dataframe['nomina(cdM)'],
            dataframe['ventas(cdm)'],
            alpha=0.5, s=45)
plt.yticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
plt.title("Ventas vs Nómina")
plt.xlabel("Nómina del área CDMX (en cientos de millones)")
plt.ylabel("Ventas(en cientos de miles)")

plt.show()

# Ecuación de la pendiente
# -- Obtener de "x^2" y "xy"
dataframe['x^2'] = dataframe['nomina(cdM)'] ** 2
dataframe['xy'] = dataframe['nomina(cdM)'] * dataframe['ventas(cdm)']

# -- Obtener los demás valores:
sumatoria_xy = dataframe['xy'].sum()
sumatoria_x2 = dataframe['x^2'].sum()
n = len(dataframe['no_años'])
media_x = dataframe['nomina(cdM)'].mean()
media_y = dataframe['ventas(cdm)'].mean()

# Ecuación de la pendiente
b = (sumatoria_xy - (n * media_x * media_y)) / \
    (sumatoria_x2 - (n * (media_x ** 2)))

# Ecuación de la ordenada
a = media_y - (b * media_x)

# es la estimación de las ventas.
x = 600000000
# convertir
x /= 100000000
# Ecuación de la recta
y = a + (b * x)

# Cálculo del error estándar de la estimación
# -- obtención de valores faltantes para la fórmula:
dataframe['y^2'] = dataframe['ventas(cdm)'] ** 2
sumatoria_y2 = dataframe['y^2'].sum()
sumatoria_y = dataframe['ventas(cdm)'].sum()

# Error estándar de la estimación:
s = ((sumatoria_y2 - (a * sumatoria_y) - (b * sumatoria_xy)) /
     (n - 2)) ** 0.5

# Cálculo del coeficiente de correlación
# -- obtener valores faltantes para la formula:
sumatoria_x = dataframe['nomina(cdM)'].sum()

# Coeficiente de correlación
r = ((n * sumatoria_xy) - (sumatoria_x * sumatoria_y)) / \
    ((((n * sumatoria_x2) - (sumatoria_x ** 2)) *
     ((n * sumatoria_y2) - (sumatoria_y ** 2))) ** 0.5)

# Coeficiente de determinación
r2 = r ** 2

print(r2)
