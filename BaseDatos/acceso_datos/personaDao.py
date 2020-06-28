import psycopg2 as db
from conexion import Conexion
from persona import Persona
from logger_base import logger

class PersonaDao():
    
    ''' 
    DAO (Data Access Object)
    CRUD: Create-Read-Update-Delete entidad Persona
    '''
    
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR    = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
    __ACTUALIZAR  = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona  = %s'
    __ELIMINAR    = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtener_cursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(
                registro[0], 
                registro[1],
                registro[2],
                registro[3]
            )
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            # conexion = Conexion.obtener_conexion()
            cursor = Conexion.obtener_cursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            
            valores = (
                persona.get_nombre(),
                persona.get_apellido(),
                persona.get_email()
            )
            
            cursor.execute(cls.__INSERTAR, valores)
            Conexion.obtener_conexion().commit()
            return cursor.rowcount
        except Exception as e:
            Conexion.obtener_conexion().rollback()
            logger.error(f'Excepción al insertar persona: {e}')
        finally:
            Conexion.cerrar()
    
    @classmethod
    def actualizar(cls, persona):
        try:
            cursor = Conexion.obtener_cursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            
            valores = (
                persona.get_nombre(),
                persona.get_apellido(),
                persona.get_email(),
                persona.get_idPersona()
            )
            
            cursor.execute(cls.__ACTUALIZAR, valores)
            Conexion.obtener_conexion().commit()
            return cursor.rowcount
            
        except Exception as e:
            Conexion.obtener_conexion().rollback()
            logger.error(f'Excepción al actualizar persona: {e}')
        finally:
            Conexion.cerrar()
    
    @classmethod
    def eliminar(cls, persona):
        try:
            cursor = Conexion.obtener_cursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            
            valores = ( persona.get_idPersona(), )
            
            cursor.execute(cls.__ELIMINAR, valores)
            Conexion.obtener_conexion().commit()
            return cursor.rowcount
            
        except Exception as e:
            Conexion.obtener_conexion().rollback()
            logger.error(f'Excepción al eliminar persona: {e}')
        finally:
            Conexion.cerrar()


#Insertar
persona = Persona(11)
registros_actualizados = PersonaDao.eliminar(persona)
logger.debug(f'Registros insertados: {registros_actualizados}')