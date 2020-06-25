
# El polimorfismo es una variable con la capacidade de apuntar a un objeto de tipo padre o tipo hijo y dependiendo de a cual a punta durante el tiempo de ejecución va a ser el método que se va a ejecutar.
# Multiples formas de ejecutar un método.

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return "El empleado se llama {} y gana ${}".format(self.nombre, self.sueldo)