"""Calificaciones de estudiantes

Crea un programa para gestionar las calificaciones de estudiantes. Usa un diccionario donde 
las claves sean los nombres de los estudiantes y los valores sean listas de calificaciones. El programa debe:

Permitir agregar nuevas calificaciones a un estudiante existente o agregar un nuevo estudiante con sus calificaciones.
Calcular y mostrar el promedio de calificaciones de cada estudiante.
Mostrar el estudiante con el promedio más alto."""

def validarEntero():
    
    while True:
        variable=input("Ingrese una opcion: ")
        if variable.isdigit():
            return int(variable)
        else:
            print("-----INGRESE UN NUMERO, POR FAVOR----")


alumnos={}
calificaciones=[]

while True:
    
    print("-----Menu----")
    print("1.Agregar Alumno")
    print("2.Agregar Nuevas Calificaciones")
    print("3.Promedio de estudiantes")
    print("4.Salir")
    
    opcion=validarEntero()
    
    if opcion==1:
        cal=[]
        nombre=input("Ingresa el nombre del estudiante")
        
        while True:
            nota=input("Ingresa la calificacion del Estudiante: ")
            cal.append(nota)
            
            sal=input("Desea agregar mas notas S/N")
            
            if sal.lower=="s":
                break
                
        print(cal)
                

