from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

control = True

while control:
    print("-> Catálogo de Peliculas <-")
    print("Elija una opción:")
    print("[1] Agregar película")
    print("[2] Listar películas")
    print("[3] Eliminar archivo de películas")
    print("[4] Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        usuario_pelicula = input("¿Qué pelicula desea agregar? R:")
        nueva_pelicula = Pelicula(usuario_pelicula)
        CatalogoPeliculas.agregar_pelicula(nueva_pelicula)
    elif opcion == 2:
        print(CatalogoPeliculas.listar_peliculas())
    elif opcion == 3:
        CatalogoPeliculas.eliminar()
    elif opcion == 4:
        control = False
    else:
        print("Ingrese una opción valida")
else:
    print("Fin de la iteración")