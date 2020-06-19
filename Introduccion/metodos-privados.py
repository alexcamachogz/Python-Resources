class Persona:
    def __init__(self, nombre, apellidoP, apellidoM):
        self.nombre = nombre # Publico
        self._apellidoP = apellidoP # Parcialmente privado o protegido
        self.__apellidoM = apellidoM # Privado
        
    def __metodo_privado(self): # Método privado
        print(self.nombre, end=" ")
        print(self._apellidoP, end=" ")
        print(self.__apellidoM)
    
    def metodo_publico(self):
        self.__metodo_privado()

p1 = Persona("Alex", "Camacho", "Gómez")
p1.metodo_publico()