class Empleado:
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario=salario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_salario(self):
        return self.salario

    def set_salario(self, value):
        self.salario = value

        
    def calcular_Bono(self):
        return float(self.salario*1.10)
    
    
class EmpleadoTiempoCompleto(Empleado):
    
    def calcular_Bono(self):
        return float(self.salario*1.15)

class EmpleadoporHora(Empleado):
        
    def calcular_Bono(self):
        return float(self.salario*1.05)
    
    
em=Empleado("ANA",2500)
em.calcular_Bono()

em2=EmpleadoporHora("SAra",2500)
em2.calcular_Bono()

em3=EmpleadoTiempoCompleto("Jorge",2500)
print(em3.calcular_Bono())
    
    