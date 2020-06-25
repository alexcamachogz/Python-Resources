from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)

empleado = Empleado("Alex", 9508.75)
imprimir_detalles(empleado)

print("-------")

gerente = Gerente("Mariana", 19605.89, "Metlife")
imprimir_detalles(gerente)
