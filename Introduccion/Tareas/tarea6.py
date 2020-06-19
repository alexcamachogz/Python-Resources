class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Es de color {} y tiene {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + " por lo tanto es un coche y su velocidad es de {} km/hr".format(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + " por lo tanto es una bicicleta y es de {}".format(self.tipo)

c1 = Bicicleta("Azul", 2, "Montaña")
print(c1)