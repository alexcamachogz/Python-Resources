import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()

# Eliminar un registro ya existente
sql = 'DELETE FROM persona WHERE id_persona IN %s'

# Eliminar más de un valor
entrada = input("Proporciona los ID a eliminar (separado por comas): ")
tupla = tuple(entrada.split(','))
llaves_primarias = (tupla,)

cursor.execute(sql, llaves_primarias)
conexion.commit()

registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

# Cierre de conexión y cursor
cursor.close()
conexion.close()