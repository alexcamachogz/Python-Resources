import os

class CatalogoPeliculas:
    
    ruta_archivo = "lista_peliculas.txt"
    
    @classmethod
    def agregar_pelicula(cls, pelicula):
        try:
            archivo = open(cls.ruta_archivo, "a")
            archivo.write(pelicula.get_nombre())
        except Exception as e:
            print("Ocurrio una excepción al agregar: ", e)
        else:
            archivo.close()
    
    @classmethod
    def listar_peliculas(cls):
        try:
            archivo = open(cls.ruta_archivo, "r")
            return archivo.read()
        except Exception as e:
            print("Ocurrio un error al listar películas: ", e)
        else:
            archivo.close()
    
    @classmethod
    def eliminar(cls):
        try:
            os.remove(cls.ruta_archivo)
            print("El archivo eliminado fue:", cls.ruta_archivo)
        except Exception as e:
            print("Ocurrio un error al eliminar el archivo. ", e)