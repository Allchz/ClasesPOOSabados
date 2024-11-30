"""Implementa un sistema para una biblioteca. Crea una clase base Publicacioncon atributos como tituloy autor. Luego, crea dos clases derivadas: Libroy Revista, con atributos adicionales como numero_paginasy numero_edicion, respectivamente. Escribe un método mostrar_informacionque
funcione para ambas clases y muestra la información específica de cada tipo de publicación."""

class Publicacion:
    def __init__(self,titulo, autor):
        self.titulo=titulo
        self.autor=autor
        
    def informacion(self):
        return f"Titulo: {self.titulo} autor: {self.autor}"
    
    
class Libro(Publicacion):
    def __init__(self, titulo, autor, numeroPaginas):
        super().__init__(titulo, autor)
        self.numeroPaginas=numeroPaginas
        
    def informacion(self):
        return super().informacion() + f"numero de Paginas {self.numeroPaginas}"
    
    
libro=Libro("Sara","Dago", 52)

print(libro.informacion())