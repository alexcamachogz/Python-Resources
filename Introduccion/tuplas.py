# Tupla -> mantiene el orden pero ya no se puede modificar

frutas = ("Manzana", "Naranja", "Uva", "Mango", "Fresa")
print(frutas)

# Largo de la tupa
print( len(frutas) )

# Accediendo a los elementos de forma individual
print( frutas[2] )

# Navegación inversa
print( frutas[-1] )

# Rangos
print( frutas[1:3] )

# La unica manera de añadir elementos a un tupla es transformandola en una lista y de vuelta a una tupla
frutasLista = list(frutas)
frutasLista[1] = "Naranjita"
frutas = tuple(frutasLista)
print(frutas)


for fruta in frutas:
    print(fruta, end=" ") # por defecto el print imprime como caracter final \n, esto puede ser reemplazado
