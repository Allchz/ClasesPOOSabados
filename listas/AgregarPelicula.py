"""Agregar y eliminar elementos en la lista: Crea una lista vacía llamada favoritos. Pide al usuario ingresar cinco películas y agrégalas a la lista.
Luego, elimina la última película de la lista e imprime el resultado."""

peliculas=[]

for p in range(5):
    pelicula=input("Ingrese una pelicula: ")
    peliculas.append(pelicula)
    
print(peliculas)

