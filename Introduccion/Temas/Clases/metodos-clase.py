class MiClase:
    variable_clase = "Variable clase"
    
    # Método estático
    @staticmethod
    def metodo_estatico():
        print("Método estático")
        # print(variable_clase) --> no se puede acceder
        print(MiClase.variable_clase)
        # Desde un método estático no podemos acceder a una variable de instancia
    
    @classmethod
    def metodo_clase(cls):
        print("Método de clase" + str(cls))
        print(cls.variable_clase)
    
    # Método de instancia
    def metodo_instancia(self):
        print("Método de instancia")
        self.metodo_clase()
        self.metodo_estatico()

MiClase.metodo_estatico()
MiClase.metodo_clase()

print('----')

obj = MiClase()
obj.metodo_instancia()