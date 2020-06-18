class Aritmetica:
    # Constructor de la clase
    def __init__(self, numeroA, numeroB):
        # Atributos de la clase
        self.numeroA = numeroA
        self.numeroB = numeroB
    
    def suma(self):
        # Se realiza la operación con los atributos de la clase
        return self.numeroA + self.numeroB
    
    def resta(self):
        return self.numeroA - self.numeroB
    
    def multiplicacion(self):
        return self.numeroA * self.numeroB
    
    def division(self):
        return self.numeroA / self.numeroB


# Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("El resultado de la suma es: {0}".format(aritmetica.suma()))