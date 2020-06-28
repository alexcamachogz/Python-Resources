import psycopg2 as db

# Información de conexión a la base de datos
conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# Cursos permite ejecutar sentencias en una base de datos
cursor = conexion.cursor()
# Sentencia
sql = 'SELECT * FROM persona ORDER BY id_persona DESC'
# Ejecución de la sentencia
cursor.execute(sql)

# Nos retorna la información proveniente de la sentencia
registros = cursor.fetchall()
print(registros)

# Cierre del cursos y de la conexión
cursor.close()
conexion.close()