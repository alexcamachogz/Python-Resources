import psycopg2 as db

conexion = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()

# %s es un comodín
sql = 'SELECT * FROM persona WHERE id_persona = %s'

id_persona = input("Proporciona tu ID: ")
llave_primaria = (id_persona,) # lo convierte en una tupla para el excecute

cursor.execute(sql, llave_primaria)
# Regresa sólo un registro
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()