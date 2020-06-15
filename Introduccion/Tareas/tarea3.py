calificacion = int( input("Ingresa tu calificacion [0-10]: ") )
nota = None

if calificacion >= 9 and calificacion <= 10:
    nota = "A"
elif calificacion == 8:
    nota = "B"
elif calificacion == 7:
    nota = "C"
elif calificacion == 6:
    nota = "D"
elif calificacion >= 0 and calificacion < 6:
    nota = "F"
else:
    nota = "Valor desconocido"

print("Tu nota equivale a una:", nota)