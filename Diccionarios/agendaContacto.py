"""Agenda de contactos

Crea un programa que administre una agenda de contactos. La agenda será un diccionario donde las claves 
sean los nombres de las personas y los valores sus números de teléfono. El programa debe permitir:

Agregar un nuevo contacto o modificar un contacto existente.
Eliminar un contacto.
Buscar un número de teléfono ingresando el nombre de una persona."""


def validarEntero():
    
    while True:
        variable=input("Ingrese una opcion: ")
        if variable.isdigit():
            return int(variable)
        else:
            print("-----INGRESE UN NUMERO, POR FAVOR----")
            
            
contacto={}




while True:
    
    print("-----Menu----")
    print("1.Agregar Contacto")
    print("2.Eliminar Contacto")
    print("3.Modificar Contacto")
    print("4.Salir")

    opcion=validarEntero()
    
    if opcion==1:
        nombre=input("Ingrese el nombre: ")
        numeroTel=input("Ingrese el numero de telefono: ")
        
        contacto[nombre]=numeroTel
    elif opcion==2:
        eliminar=input("Ingrese el nombre que desea eliminar: ")
       
        if eliminar in contacto:
            del contacto[eliminar]
    elif opcion==3:
        modificar=input("Que contacto desea modificar")
        
        if modificar in contacto:
            nuevonum=input("Ingrese el nuevo numero: ")
            
            contacto[modificar]=nuevonum
        else:
            print("Ese contacto no existe")     
    elif opcion==4:
        break
    print(contacto)
        