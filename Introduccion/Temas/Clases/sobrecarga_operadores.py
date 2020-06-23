class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Método sobreescrito de la clase padre object
    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre
    
    def __sub__(self, otro):
        return "Operación no soportada"

p1 = Persona("Alex")
p2 = Persona("Matty")

# Nueva forma de trabajar el operador +
print(p1 + p2)
print(p1 - p2)


# + es un ejemplo de sobrecarga
# a = 2
# b = 3
# print(a + b)

# st1 = "Hola "
# st2 = "Mundo"
# print(st1 + st2)

# list1 = [1, 2]
# list2 = [4, 5]
# print( list1 + list2 )