# ---------------------
#        ETAPA I      -
#   christian campos  -
# ---------------------

# install.packages('rpart')
# install.packages('caret')
# install.packages('tree')

library(datasets)
library(rpart)
library(caret)

# dataset Iris
data(iris)

# Selección de columnas del data set
iris_date <- iris[, c("Sepal.Width", "Petal.Width", "Species")]

# Semilla
set.seed(123)

# Dividir datos en entrenamiento y prueba (70% - 30%)
trainIndex <- createDataPartition(iris_data$Species, p = 0.7, list = FALSE)
trainData <- iris_data[trainIndex, ]
testData <- iris_data[-trainIndex, ]

# Entrenamiento del modelo
tree_model <- rpart(Species ~ Sepal.Width + Petal.Width, 
                    data = trainData, method = "class")

# Obtener probabilidades de clasificación y Mostrarlas
probabilities <- predict(tree_model, newdata = testData, type = "prob")
head(probabilities)


# Realizar predicciones en los datos de prueba
predictions <- predict(tree_model, newdata = testData, type = "class")
# Crear tabla de predicciones
prediction_table <- data.frame(Actual = testData$Species, 
                               Predicted = predictions)
# Mostrar primeras observaciones
head(prediction_table)
# Calular precisión del modelo
confusion_matrix <- confusionMatrix(predictions, testData$Species)
print(confusion_matrix)


# Ilustración del árbol
library(rpart.plot)
rpart.plot(tree_model)


# Podado
library(tree)
# conversion de modelo para usar prune.tree
tree_model_tree <- tree(Species ~ Sepal.Width + Petal.Width, data = trainData)
# podar para obtener 4 hojas
pruned_tree <- prune.tree(tree_model_tree, best = 4)
#Visualizar árbol podado
plot(pruned_tree)
text(pruned_tree)