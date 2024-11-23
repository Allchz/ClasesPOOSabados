"""Encuesta de opiniones

Diseña un programa que recopile opiniones de personas sobre una película. El programa debe permitir al usuario ingresar el nombre de 
una persona y su calificación (entre 1 y 5). Usa un diccionario para almacenar los datos, donde las claves sean los nombres y 
los valores las calificaciones. Finalmente, el programa debe:

Mostrar la calificación promedio de la película.
Indicar cuántas personas dieron una calificación mayor o igual a 4."""


def validarentero():

    while True:
        variable = input("Ingrese la opcion:")
        if variable.isdigit():
            return int(variable)
        else:
            print("-----Por favor, Ingrese un numero-------")
            
            


calificacion=[]
dic={}     
while True:
 
    print("Menu")
    print("1.Ingresar Valoracion")
    print("2.Ver Promedio")
    print("3.Salir")
    
    opcion=validarentero()
    
    if opcion==1:
        nombre=input("Ingrese su nombre")
        
        try:
            calificacion = int(input("Calificación (entre 1 y 5): "))
            if 1 <= calificacion <= 5:
                dic[nombre] = calificacion
            else:
                print("Por favor, ingresa una calificación válida (1-5).")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entre 1 y 5.")
    elif opcion==2:
        sumValoracion=sum(dic.values())
        promedio=sumValoracion/len(dic)
        
        print(f"el promedio es {promedio} ")
        
        suma=0
        for calificacion in dic.values():
            if calificacion>4:
                suma+=1
             
        print(suma)
            
        
            
        
        


    