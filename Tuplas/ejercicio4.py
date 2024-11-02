"""Crea una tupla que contenga números, algunos de ellos repetidos. Cuenta cuántas veces aparece el número 5."""


# Crear la tupla
numeros = (1, 2, 5, 3, 5, 4, 5, 6, 5)

# Contar las ocurrencias de 5
conteo_5 = numeros.count(5)
print("El número 5 aparece", conteo_5, "veces.")