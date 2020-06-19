class Persona:
    def __init__(self, nombre, edad, *valores, **diccionario): # * indica un parámtro opcional
        self.nombre = nombre
        self.edad = edad
        self.valores = valores
        self.diccionario = diccionario
    
    def desplegar(self):
        print("Su nombre es {0} y tiene {1} años".format(self.nombre, self.edad))
        print("Valores (tupla):", self.valores)
        print("El diccionario contiene:", self.diccionario)
        print()

p1 = Persona("Alex", 26)
p1.desplegar()

p2 = Persona("Matty", 24, 21,1,2012)
p2.desplegar()

p3 = Persona("Hector", 28, 4,9, m="manzana", p="pera", j="jicama")
p3.desplegar()