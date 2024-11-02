"""Crea un programa que pida al usuario una palabra y un número entero n.
El programa debe generar una nueva cadena que contenga cada n-ésima letra de la palabra original."""

palabra=input("Ingrese una palabra:")
num=int(input("Ingrese un numero: "))

if num<=len(palabra):
    nuevapalabra=palabra[num:]
    print(nuevapalabra)
else:
    print("Ingrese otro numero o numero invalido")


