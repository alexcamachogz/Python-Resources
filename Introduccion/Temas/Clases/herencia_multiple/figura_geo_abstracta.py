
#ABC Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    @abstractmethod
    def area(self):
        pass