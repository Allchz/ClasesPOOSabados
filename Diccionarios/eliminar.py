"""Dado el diccionario {"Python": "Lenguaje de programación", "HTML": "Lenguaje de marcado", "CSS": "Estilos de página"}, 
elimina la clave "CSS"y muestra el diccionario resultante."""

programas={"Python": "Lenguaje de programación", "HTML": "Lenguaje de marcado", "CSS": "Estilos de página"}

del programas["CSS"]

print(programas)