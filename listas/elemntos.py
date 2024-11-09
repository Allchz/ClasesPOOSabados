"""Listar elementos comunes entre dos listas: Dadas dos listas, lista1 = [1, 2, 3, 4, 5] y lista2 = [4, 5, 6, 7, 8], 
crea una nueva lista que contenga los elementos que están en ambas listas."""

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Encontrar elementos comunes utilizando la intersección de conjuntos
elementos_comunes = list(set(lista1) & set(lista2))
print("Elementos comunes entre las dos listas:", elementos_comunes)