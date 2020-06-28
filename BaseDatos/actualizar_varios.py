import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()

# Actualizar un registro ya existente
sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona  = %s'

# Insertar más de un registro
valores = (
    ('Carlos', 'Lara', 'carlos@gmail.com', 8),
    ('Julio2', 'de la Torre2', 'julio2@gmail.com', 9),
)

cursor.executemany(sql, valores)

# Guardar la información en la bade de datos
conexion.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

# Cierre de conexión y cursor
cursor.close()
conexion.close()
