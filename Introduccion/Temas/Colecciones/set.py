# Set es una colección sin orden y sin indices

planetas = {"Marte", "Júpiter", "Venus"}
print(planetas)

# Longitud del set
print( len(planetas) )

# Revisar si un elemento está presente
print("Marte" in planetas)

# Agregar nuevos elementos
planetas.add("Tierra")
print(planetas)

# Eliminar elementos
planetas.remove("Tierra")
print(planetas)
# Eliminar con discard, no arroja excepción si no encuentra el elemento a eliminar
planetas.discard("Júpiter")
print(planetas)

# Limpiar el set completamente
planetas.clear()
print(planetas)

# Eliminar completamente la variable
del planetas