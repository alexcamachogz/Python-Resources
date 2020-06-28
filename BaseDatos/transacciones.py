import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# Guarda los cambios de forma automática, esta propiedad sólo se usa para pruebas
# conexion.autocommit = True
try:
    cursor = conexion.cursor()
    sql = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
    valores = ('Carolina2', 'Ortiz2', 'carolina2@gmail.com')
    
    sql2 = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona  = %s'
    valores2 = ('Julio2', 'de la Torre2', 'julio2@gmail.com', 11)
    
    # Ejecución de la sentencia
    cursor.execute(sql, valores)
    cursor.execute(sql2, valores2)
    conexion.commit()
except Exception as e:
    # rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrio un error en la transacción: {e}')
finally:
    # Cierre de conexión y cursor
    cursor.close()
    conexion.close()
