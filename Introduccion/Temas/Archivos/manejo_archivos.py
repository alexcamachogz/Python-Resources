
try:
    # Si no existe el archivo lo crea en la ruta que estemos trabajando
    archivo = open("prueba.txt", "w")
    archivo.write("Me llamo Alejandra Camacho.\n")
    archivo.write("Estoy estudiando un curso de Python.")
except Exception as e:
    print(e)
finally:
    # Cierra el archivo cuando se termina de utilizar.
    archivo.close()