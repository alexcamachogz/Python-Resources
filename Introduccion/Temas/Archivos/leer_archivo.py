
# Trabajar con un archivo que no se encuentra en la misma ruta
archivo = open("/Users/alejandracamacho/Documents/Repositorios/Python/Introduccion/prueba.txt", "r")
# print(archivo.read())

# Leer algunos caracteres
print(archivo.read(5))

# Leer lineas completas de un archivo
print(archivo.readline())

# Iterando las lineas del archivo
# for linea in archivo:
#     print(linea)

# Leer todas las lineas del archivo, retorna una lista con todas las líneas del archivo
# print(archivo.readlines())

# Acceder a una línea en especifico
print(archivo.readlines()[2])

# Abrir un nuevo archivo, para copiar un archivo dentro de otro
archivo2 = open("copia.txt", "a") # Se añade el nuevo contenido sin eliminar el anterior
archivo2 = open("copia.txt", "w") # El archivo se reescribirar desde cero en cada ocasión
archivo2.write(archivo.read())

archivo.close()
archivo2.close()