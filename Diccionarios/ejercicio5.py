"""Almacenamiento de Información: Escribe un programa que almacene 
información sobre estudiantes (nombre, edad, y nota) en un diccionario. 
Permite al usuario agregar nuevos estudiantes y mostrar la lista completa.

"""
def menu():
    print("---Elija una opcion---")
    print("1.Agregar estudiante")
    print("2.Visualizar")
    print("3.Salir")
    
alumno={}

while True:
    
    menu()
    
    opcion=int(input("Ingrese una Opcion: "))
    
    if opcion==1:
      
        alumno["nombre"]=input("Ingrese el nombre del alumno: ")
        alumno["edad"]=int(input("Ingrese la edad"))
        alumno["nota"]=int(input("Ogrese la nota del alumno: "))
        
        
    if opcion==2:
        if alumno:
            print("\nLista de estudiantes:")
            for nombre in alumno.items():
                print(f"Nombre: {nombre},")
        else:
            print("No hay estudiantes registrados.\n")

    if opcion==3:
        break
        





