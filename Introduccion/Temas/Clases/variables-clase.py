class MiClase:
    variable_clase = "Variable de Clase" # Esta es una variable de clase
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia # Esto es una variable de instancia

# Se puede acceder sin crear un objeto
print(MiClase.variable_clase)
# No se puede acceder sin la instancia de un objeto que lo inicializa 
# print(MiClase.variable_instancia)

MiClase.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia) # Valores distintos

objeto = MiClase("Variable instancia")
print(objeto.variable_instancia) # Valores distintos

# Podemos acceder a las variables de clase desde los objetos
print(objeto.variable_clase)
# Podemos acceder a las variables de clase desde la clase
print(MiClase.variable_clase)

objeto.variable_clase = "Modificando variable de clase" # Este cambio se asocia sólo al objeto


