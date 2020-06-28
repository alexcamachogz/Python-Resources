# Clase Orden

class Orden:
    
    contador_ordenes = 0
    
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        #Recibe la lista de objetos de tipo Computadora
        self.__computadoras = computadoras  
    
    def __str__(self):
        computadora_str = ""
        for computadora in self.__computadoras:
            computadora_str += computadora.__str__()
        return(
            f"Orden: {self.__id_orden}"
            f"Computadoras: {computadora_str}"
        )
    
    def agregarComputadora(self, computadora):
        self.__computadoras.append(computadora)
    
    # Métodos get y set
    def get_idOrden(self):
        return self.__id_orden
    
    def set_idOrden(self, num):
        self.__id_orden = num
    
    def get_computadoras(self):
        return self.__computadoras
    
    def set_computadoras(self, computadora):
        self.__computadoras = computadora