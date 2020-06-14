print("Proporcione los siguientes datos del libro:")
nombre = input("Proporcione el nombre del libro: ")
id = int( input("Poporcione el ID:") )
precio = float( input("Proporcione el precio: $") )
envioGratuito = input("Indica si el envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    print("Ingresaste un valor invalido para el envio gratuito")
    envioGratuito = "Valor incorrecto, debe ser True/False"
    
print(" ---> Datos del Libro <---")
print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)
print("¿Tiene envio gratis?", envioGratuito)