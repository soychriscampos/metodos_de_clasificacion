# material/ejercicio de clase
install.packages('titanic')

# lib de análisis
library(tidyverse)

#lib de datos
library(titanic)
data("titanic_train")
head(titanic_train)

#librerías para clasificación
install.packages("rpart")
library(rpart)
install.packages("rattle")
library(rattle)
install.packages("rpart.plot")
library(rpart.plot)

# modelando árboles de decisión
arbol <- rpart(
  formula = Survived ~ Sex + Age,
  data = titanic_train,
  method = 'class'
)

# graficando el arbol
fancyRpartPlot(arbol)
