"""Crea un programa que lea un archivo de texto llamado datos.txt y 
muestre por pantalla cuántas líneas tiene y el contenido de cada línea."""

archivo= open("Practica26/ficheros/datos.txt","r")


contador=0
for linea in archivo:
    contador+=1

print(f"HAY {contador} lienas")
    
