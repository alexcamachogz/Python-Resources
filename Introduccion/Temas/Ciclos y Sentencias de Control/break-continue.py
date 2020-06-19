

# Imprimir sólo la primera letra A que se encuentre
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break # Termina la ejecución del ciclo, se salta incluso el else
else:
    print("Fin Ciclo")
    
# Imprimir sólo números pares dentro de un rango
for i in range(6): # range es una función que imprime desde el 0 hasta -1 del número pasado como parámetro
    if i % 2 != 0:
        continue # Salta la ejecución e inicia la siguiente iteración
    print(i)