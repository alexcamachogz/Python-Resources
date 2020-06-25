from numeros_identicos_except import NumerosIdenticosException

c = None

try:
    a = int( input("Primer número: ") )
    b = int( input("Segundo número: ") )
    
    if a == b:
        raise NumerosIdenticosException("Numéros Indenticos")
    
    c = a / b
except Exception as e:
    print("Ocurrio un error:", e)
    print(type(e))
else: # Se ejecuta sólo si no hubo excepciones
    print("No hubo ninguna excepción")
finally: # Siempre se ejecuta
    print("Fin del manejo de excepciones")

print("Resultado:", c)
print("Continuamos...")