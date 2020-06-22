
class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
    
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " | "
        return "Orden: {}, Productos: {}".format(self.__id_orden, productos_str)
    
    def agregar_producto(self, nuevoProducto):
        self.__productos.append(nuevoProducto)
    
    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total