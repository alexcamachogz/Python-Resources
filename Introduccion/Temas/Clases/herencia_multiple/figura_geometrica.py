class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    def __str__(self):
        return "El ancho es de {}, el alto es de {}.".format(self.__ancho, self.__alto)
    
    # Getter
    def get_ancho(self):
        return self.__ancho
    
    def get_alto(self):
        return self.__alto
    
    # Setter
    def set_ancho(self, ancho):
        self.__ancho = ancho
    
    def set_alto(self, alto):
        self.__alto = alto