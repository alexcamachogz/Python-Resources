
# Definición de una lista
nombres = [ 'Alejandra', 'Vanessa', 'Laura', 'Mariana']

# Conocer el largo de la lista
print( len(nombres) )

# Acceder al elemento según su posición en la lista
nombres[0] # En este caso accede al elemento 'Alejandra'

#navegación inversa
print( nombres[-1] ) # Se solicita el último elemento de nuestra lista
print( nombres[-2] ) # Penultimo elemento

# Imprimir un rango
print( nombres[0:2] ) # Se recuperan los indices del 0 al 2 sin incluir el 2

# Imprimir los elementos desde el inicio hasta el indice proporcionado
print( nombres[:3] ) # Omite el 3

# Imprimir los elementos hasta le final desde el indice proporcionado
print( nombres[1:] )

# Cambiar los elementos de una lista
nombres[3] = "Carmen"
print(nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)

# Revisar si existe un elemento en la lista
if "Laura" in nombres:
    print("Si existe!")
else:
    print("El elemento buscado no existe en la lista")

# Agregar un nuevo elemento al final de la lista
nombres.append("Aldo")
print(nombres)

# Agregar un nuevo elemento en el indice proporcionado
nombres.insert(1, "Ángel") # Se imprime antes del inidice indicado
print(nombres)

# Remover un elemento de nuestra lista
nombres.remove("Vanessa")
print(nombres)

# Remover el último elemento de la lista
nombres.pop()
print(nombres)

# Remover el inidice indicado de la lista
del nombres[0]
print(nombres)

# Si no se especifica un indice al del remueve toda la variable

# Limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)

del nombres

