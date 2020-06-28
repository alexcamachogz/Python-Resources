class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        # Atributos protegidos ( accesibles desde una sub-clase )
        self._tipoEntrada = tipoEntrada
        self._marca = marca
    
    def __str__(self):
        return "El dispositivo es un {} de la marca {}".format(self.tipoEntrada, self.marca)
    
    def get_tipoEntrada(self):
        return self._tipoEntrada
    
    def set_tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada
    
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca):
        self._marca = marca