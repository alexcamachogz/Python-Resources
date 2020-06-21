from figura_geo_abstracta import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def __str__(self):
        return super().__str__() + " y el color es " + self.get_color() + "."
    
    def area(self):
        return self.get_alto() * self.get_ancho()