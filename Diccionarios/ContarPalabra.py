"""Contar palabras
Escribe una función que reciba una lista de palabras y devuelva un diccionario con cada palabra 
como clave y el número de veces que aparece en la lista como valor.
Ejemplo:
Entrada: ["manzana", "pera", "manzana", "naranja", "pera", "pera"]
Salida:{"manzana": 2, "pera": 3, "naranja": 1}"""


def contar(lista):
     # Crear un diccionario vacío
    conteo = {}
    
    # Recorrer cada palabra en la lista
    for palabra in lista:
        if palabra in conteo:
            conteo[palabra] += 1  # Incrementar el contador si ya existe la palabra
        else:
            conteo[palabra] = 1  # Añadir la palabra al diccionario con un conteo inicial de 1
    return conteo


palabras=["manzana", "pera", "manzana", "naranja", "pera", "pera"]

print(contar(palabras))


    
    
    
    