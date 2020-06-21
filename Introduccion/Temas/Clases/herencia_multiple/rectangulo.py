from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def area(self):
        return self.get_alto() * self.get_ancho()
    
    def __str__(self):
        return super().__str__() + " y el color es " + self.get_color() + "."

rectangulo = Rectangulo(5, 10, "Verde")
print(rectangulo.area())
print(rectangulo.__str__())