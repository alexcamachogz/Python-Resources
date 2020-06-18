
# Definición de la clase
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

# Solictar variables al usuario
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

# Creación de la instancia de la clase
rect = Rectangulo(base, altura)

# Entregar resultados
print("El área del rectangulo es: {0}".format(rect.area()))