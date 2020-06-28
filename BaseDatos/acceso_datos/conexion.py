import psycopg2 as db
import sys
from logger_base import logger

class Conexion:
    __DATABASE  = 'test_db'
    __USERNAME  = 'postgres'
    __PASSWORD  = 'admin'
    __DB_PORT   = '5432'
    __HOST      = '127.0.0.1'
    __conexion  = None
    __cursor    = None
    
    @classmethod
    def obtener_conexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion  = db.connect(
                    user        = cls.__USERNAME,
                    password    = cls.__PASSWORD,
                    host        = cls.__HOST,
                    port        = cls.__DB_PORT,
                    database    = cls.__DATABASE
                )
                logger.debug(f'Conexión exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la BD: {e}')
                sys.exit() # Termina la ejecución de nuestro programa
        else:
            return cls.__conexion
    
    @classmethod
    def obtener_cursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtener_conexion().cursor()
                return cls.__cursor
                logger.debug('Se abrio el cursor con éxito: {cls.__cursor}')
            except Exception as e:
                logger.error(f'Error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor
    
    @classmethod 
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Error al cerrar el cursor: {e}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.error(f'Error al cerrar la conexión: {e}')
        logger.debug('Se han cerrado los objetos de conexión y cursor')