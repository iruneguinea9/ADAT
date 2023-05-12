import mysql.connector

conDB=mysql.connector.connect(user='admin', password='password',
                               host='localhost',
                               database='aeropuertos')
# cursor para ejecutar consulta
cursor = conDB.cursor()

with open("pruebas.sql") as f:
    sql = f.read()
resultados = cursor.execute(sql, multi=True)
try:
    for r in resultados:
        print(r)
except Exception as e:
    print("FIN")

sql = "create table alumnos3(id int(11))"
cursor.execute(sql)

# cerrar cursor
cursor.close()
# cerrar conexion
conDB.close()