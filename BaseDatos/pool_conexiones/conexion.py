from psycopg2 import pool
import sys
from logger_base import logger

class Conexion:
    # Constantes
    __DATABASE  = 'test_db'
    __USERNAME  = 'postgres'
    __PASSWORD  = 'admin'
    __DB_PORT   = '5432'
    __HOST      = '127.0.0.1'
    __MIN_CON   = 1
    __MAX_CON   = 5
    # Variables
    __pool      = None
    # __conexion  = None
    # __cursor    = None
    
    @classmethod
    def obtener_pool(cls):
        if cls.__pool is None:
            try:
                # Abrir pool de conexiones
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    user        = cls.__USERNAME,
                    password    = cls.__PASSWORD,
                    host        = cls.__HOST,
                    port        = cls.__DB_PORT,
                    database    = cls.__DATABASE
                )
                logger.debug(f'Pool creado: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al crear el pool: {e}')
                sys.exit() # Termina la ejecución de nuestro programa
        else:
            return cls.__pool
    
    @classmethod
    def liberar_conexion(cls, conexion):
        # Regresar el objeto conexion al pool
        cls.obtener_pool().putconn(conexion)
        logger.debug(f'Regresamos la conexión al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
    
    @classmethod
    def obtener_conexion(cls):
        # Obtener una conexión del objeto pool
        conexion = cls.obtener_pool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def cerrar_conexiones(cls):
        # Cerrar el pool y todas sus conexiones
        cls.obtener_pool().closeall()
        logger.debug(f'Se cerraron todas las conexiones del pool: {cls.__pool}')