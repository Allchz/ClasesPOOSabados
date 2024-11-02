"""Escribe un programa que copie el contenido de un archivo llamado origen.txt a otro archivo llamado destino.txt."""


with open( "Practica26/ficheros/origen.txt","r") as fichero,  open("Practica26/ficheros/destino.txt","w") as destino:
    for linea in fichero:
        destino.write(linea)


with open("Practica26/ficheros/destino.txt","r") as destino:
    contenido=destino.read()
    
print(contenido)