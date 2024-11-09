"""Convertir tupla en lista: Dada una tupla 
numeros = (10, 20, 30, 40), conviértela en una lista y añade el 
número 50. Luego, convierte la lista nuevamente en tupla e imprímela."""

numeros = (10, 20, 30, 40)

listaNum=list(numeros)

listaNum.append("50")

nuevatupla=tuple(listaNum)

print(nuevatupla)


