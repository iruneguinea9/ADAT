# Conexión con base de datos

# importar paquete
import mysql.connector

# conectar
conn = mysql.connector.connect(user='admin', password='password',
                               host='localhost',
                               database='aeropuertos')

# cursor para ejecutar consulta
cursor = conn.cursor()

cursor.execute("SELECT * FROM aviones")

# recoger los resultados de la consulta
resultados = cursor.fetchall()


# imprimir resultados
for x in resultados:
    print(x)

# cerrar cursor
cursor.close()
# cerrar conexion
conn.close()
