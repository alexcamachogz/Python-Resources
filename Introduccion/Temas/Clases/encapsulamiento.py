# Clase persona
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre # __ indica que es una variable es privada
    
    def getNombre(self): # Permite obtener el valor del atributo privado
        return self.__nombre
    
    def setNombre(self, nombre): # Permite modificar el valor del atributo privado
        self.__nombre = nombre

p1 = Persona("Alex")
print(p1.getNombre()) # Obtiene el nombre

p1.setNombre("Alejandra") # Modifica el nombre
print(p1.getNombre())