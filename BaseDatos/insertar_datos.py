import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sql = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'

# Insertar más de un registro
valores = (
    ('Carlos', 'Lara', 'carlos@gmail.com'),
    ('Julio', 'de la Torre', 'julio@gmail.com'),
    ('Carolina', 'Ortiz', 'carolina@gmail.com')
)
cursor.executemany(sql, valores)

# Guardar la información en la bade de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

# Cierre de conexión y cursor
cursor.close()
conexion.close()