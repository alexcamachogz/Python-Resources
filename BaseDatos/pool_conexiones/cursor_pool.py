from conexion import Conexion
from logger_base import logger

class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    # Inicio de la sintaxis de with
    #inicio de with
    def __enter__(self):
        logger.debug('Inicio de with método __enter__') 
        self.__conn = Conexion.obtener_conexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    
    # Fin del bloque with
    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug(f'Se ejecuta el método __exit__')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transacción')
        # Cerramos el cursor
        self.__cursor.close()
        # Regresar la conexión al pool
        Conexion.liberar_conexion(self.__conn)