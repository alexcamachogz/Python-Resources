
# Diccionario

diccionario = {
    "IDE"   : "Integrated Development Environment",
    "OOP"   : "Object Oriented Programming",
    "DBMS"  : "Database Management System"
}

print(diccionario)

# Longitud del diccionario
print ( len(diccionario) )

# Accediendo a un elemento
print( diccionario["IDE"])
print( diccionario.get("OOP"))

# Modificando valores
diccionario["IDE"] = "Integretad development environment"

print(diccionario)

# Iteración de elementos
for key in diccionario:
    print( key )
for value in diccionario:
    print(diccionario[value])

for valor in diccionario.values():
    print(valor)

# Comprobar si un elemento existe en el diccionario
print( "IDE" in diccionario)

# Agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover elementos del diccionario
diccionario.pop("DBMS")
print(diccionario)

# Limpiar 
diccionario.clear()
print(diccionario)

# Remover la variable del diccionario
del diccionario