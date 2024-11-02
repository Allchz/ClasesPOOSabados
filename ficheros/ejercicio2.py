"""scribe un programa que pida al usuario una serie de nombres y los guarde en un archivo llamado nombres.txt. 
Luego, el programa debe leer el archivo y mostrar los nombres guardados."""
with open( "Practica26/ficheros/nombres.txt", 'w') as f:
    while True:
        nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        f.write(nombre + "\n")

# Leer y mostrar el contenido del archivo
with open("Practica26/ficheros/nombres.txt", 'r') as f:
    contenido_nombres = f.readlines()

# Mostrar cada nombre
print("\nNombres guardados en el archivo:")
for nombre in contenido_nombres:
    print(nombre.strip())


    
