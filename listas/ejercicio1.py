"""Crea un programa que genere una lista de los primeros 100 números enteros y muestre la suma de todos los números."""

numeros = list(range(1, 101))

# Calcular la suma de todos los números en la lista
suma_numeros = sum(numeros)

# Mostrar resultados
print("Lista de los primeros 100 números enteros:")
print(numeros)
print("\nSuma de los primeros 100 números enteros:", suma_numeros)