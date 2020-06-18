# Clases

# Sintaxis básica
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear un objeto, nueva instancia de la clase
persona = Persona("Alejandra", 26)
print(persona.nombre)
print(persona.edad)

print ("Tu nombre es {0} y tienes {1} años.".format(persona.nombre, persona.edad))
