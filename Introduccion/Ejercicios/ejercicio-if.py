mes = int( input("Ingrese el mes de su elección [1-12]: ") )
estacion = None

if (mes >= 1 and mes <= 2) or mes == 12:
    estacion = "Invierno"
elif mes >= 3 and mes <= 5:
    estacion = "Primavera"
elif mes >= 6 and mes <= 8:
    estacion = "Verano"
elif mes >= 9 and mes <= 11:
    estacion = "Otoño"
else:
    estacion = "Mes fuera de rango"
    
print( "Estación:", estacion, "para el mes", mes)