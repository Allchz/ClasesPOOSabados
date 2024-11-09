"""Verificar elemento en tupla: Dada una tupla de números del 1 al 5, 
escribe un programa que verifique si el número 3 está en la tupla e imprima el resultado."""

tupla=tuple(range(1,6))
print(tupla)

if 3 in tupla:
    print("El numero 3 se encuentra en la tupla")
else:
    print("No hay nada")