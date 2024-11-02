"""Escribe un programa que solicita al usuario ingresar una frase. Luego, realiza las siguientes operaciones:

Encuentra la primera aparición de la palabra "Python"en la frase, e imprime su posición.
Convierta la frase a mayúsculas y luego a minúsculas, mostrando ambos resultados.
Extrae una subcadena que incluye solo las tres primeras y tres últimas letras de la frase, y muestra el resultado."""


palabra= input(" Ingrese una palabra: ")

posicion=palabra.find("Python")
mayuscula=palabra.upper()
minuscula=palabra.lower()

print(f"la palabra Pythn se encuengra en la posisicion {posicion}")
print(f"La frase en Mayuscula: {mayuscula}")
print(f"La frase en Minuscula: {minuscula}")