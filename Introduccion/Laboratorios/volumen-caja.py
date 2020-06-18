
# Definición de la clase
class Caja:
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    
    def volumen(self):
        return self.largo * self.ancho * self.alto

# Pidiendo valores al usuario
largo = int( input("Indique el largo de la caja: ") )
ancho = int( input("Indique el ancho de la caja: ") )
alto  = int( input("Indique el alto  de la caja: ") )

# Creando instancia de la clase
caja = Caja( largo, ancho, alto )

# Resultado
print("Con los valores {0} de largo, {1} de ancho y {2} de alto, el volumen de la caja es de: {3} m3".format(largo, ancho, alto, caja.volumen()))