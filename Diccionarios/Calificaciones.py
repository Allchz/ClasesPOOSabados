"""Calificaciones de estudiantes

Crea un programa para gestionar las calificaciones de estudiantes. Usa un diccionario donde 
las claves sean los nombres de los estudiantes y los valores sean listas de calificaciones. El programa debe:

Permitir agregar nuevas calificaciones a un estudiante existente o agregar un nuevo estudiante con sus calificaciones.
Calcular y mostrar el promedio de calificaciones de cada estudiante.
Mostrar el estudiante con el promedio más alto."""

# Diccionario para almacenar estudiantes y calificaciones
estudiantes = {}

while True:
    print("\n--- Gestión de Calificaciones ---")
    print("1. Agregar calificaciones")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor promedio")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        # Agregar o modificar calificaciones
        nombre = input("Nombre del estudiante: ")
        calificaciones = input("Calificaciones (separadas por comas): ")
        calificaciones = [float(c) for c in calificaciones.split(",")]  # Convertir a números
        if nombre in estudiantes:
            estudiantes[nombre].extend(calificaciones)  # Agregar a las existentes
        else:
            estudiantes[nombre] = calificaciones  # Crear nueva entrada
        print(f"Calificaciones actualizadas para {nombre}: {estudiantes[nombre]}")

    elif opcion == "2":
        # Mostrar promedios de calificaciones
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for nombre, calificaciones in estudiantes.items():
                promedio = sum(calificaciones) / len(calificaciones)  # Calcular promedio
                print(f"{nombre}: Promedio = {promedio:.2f}")

    elif opcion == "3":
        # Mostrar estudiante con mejor promedio
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            mejor_estudiante = None
            mejor_promedio = 0
            for nombre, calificaciones in estudiantes.items():
                promedio = sum(calificaciones) / len(calificaciones)  # Calcular promedio
                if promedio > mejor_promedio:
                    mejor_promedio = promedio
                    mejor_estudiante = nombre
            print(f"Mejor promedio: {mejor_estudiante} con {mejor_promedio:.2f}")

    elif opcion == "4":
        print("¡Adiós!")
        break

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
