"""Buscar un elemento en la lista: Crea una lista con nombres de países. Luego, escribe un programa que le pida al usuario ingresar un país y determine si ese país está en la lista o no."""
paises=["Francia", "Venezuela", "Rusia", "Marruecos", "Honduras"]

buscar=input("Ingrese el pais a Buscar: ")

if buscar in paises:
    print(f" {buscar} esta en la lista")
else:
    print(" No se encuentra en la lista")