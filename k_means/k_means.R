library(ggplot2)
# -------------------------------------
#             1 CREAR DATOS           -
# -------------------------------------
# Los datos se crean de manera aleatoria
set.seed(123)
n <- 100
data <- data.frame(
  x = rnorm(n, mean = rep(c(2, 5), each = n / 2), sd = 0.5),
  y = rnorm(n, mean = rep(c(2, 5), each = n / 2), sd = 0.5)
)

# -------------------------------------
# 2 CREAR FUNCIÓN QUE CREE CENTROIDES -
# -------------------------------------
# Función para inicializar centroides aleatorios
initialize_centroids <- function(data, k) {
  set.seed(123)
  centroids <- data[sample(1:nrow(data), k), ]
  return(centroids)
}

# Definir el número de clusters
k <- 3
centroids <- initialize_centroids(data, k)
print(centroids)

# -------------------------------------
#               ADICIONAL             -
# -------------------------------------
# Asignar puntos a los clusters
# Función para asignar puntos a los clusters más cercanos
assign_clusters <- function(data, centroids) {
  distances <- as.matrix(dist(rbind(data, centroids)))
  distances <- distances[1:nrow(data), (nrow(data) + 1):(nrow(data) + nrow(centroids))]
  clusters <- apply(distances, 1, which.min)
  return(clusters)
}

data$cluster <- assign_clusters(data, centroids)

# ------------------------------------------
#   3 DIBUJAR GRÁFICA CLUSTERS Y ERRORES   -
# ------------------------------------------
# Calcular la distancia al cuadrado de la primera observación a cada centroide
first_observation <- data[1, ]
squared_errors <- apply(centroids, 1, function(centroid) {
  sum((first_observation - centroid)^2)
})

# Crear un data frame para los errores al cuadrado
squared_errors_df <- data.frame(
  centroid = 1:k,
  squared_error = squared_errors
)

# Graficar los datos coloreados por cluster
ggplot(data, aes(x = x, y = y, color = as.factor(cluster))) +
  geom_point() +
  geom_point(data = centroids, aes(x = x, y = y), color = "black", size = 4) +
  labs(title = "Distribución de Datos y Centroides",
       x = "X",
       y = "Y",
       color = "Cluster")

# Graficar el error al cuadrado de la primera observación sobre cada centroide
ggplot(squared_errors_df, aes(x = factor(centroid), y = squared_error)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Error al Cuadrado de la Primera Observación sobre Cada Centroide",
       x = "Centroide",
       y = "Error al Cuadrado")
