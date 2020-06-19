
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad:" + str(self.edad)

# Empleado hereda de la clase persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Se accede al constuctor de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo;
    
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)

sujeto = Persona("Alex", 26)
print(sujeto)

empleado = Empleado("Mariana", 24, 9400.50)
print(empleado)
