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
sql = 'SELECT * FROM persona WHERE id_persona IN %s'

# Busqueda dinámica
entrada = input("Proporciona los ID a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
llaves_primarias = (tupla,) # lo convierte en una tupla de tuplas para el excecute

cursor.executemany(sql, llaves_primarias)
# Regresa sólo un registro
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conexion.close()