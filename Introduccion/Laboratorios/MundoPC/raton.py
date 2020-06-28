from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipoEntrada):
        super().__init__(tipoEntrada, marca)
        Raton.contador_ratones += 1
        self.__id_raton = self.contador_ratones
        # self._marca = marca
        # self._tipoEntrada = tipoEntrada
    
    def __str__(self):
        return (
            # Formato de tipo cade<
            f"ID: {self.__id_raton}, "
            f"Marca: {self._marca}, "
            f"Tipo de entrada: {self._tipoEntrada}"
        )