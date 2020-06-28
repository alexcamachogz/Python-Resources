from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, marca, tipoEntrada):
        super().__init__(tipoEntrada, marca)
        Teclado.contador_teclados += 1
        self.__id_teclado = self.contador_teclados
    
    def __str__(self):
        return (
            # Formato de tipo cade<
            f"ID: {self.__id_teclado}, "
            f"Marca: {self._marca}, "
            f"Tipo de entrada: {self._tipoEntrada}"
        )

tcl = Teclado("Acer", "USB-C")
print(tcl)