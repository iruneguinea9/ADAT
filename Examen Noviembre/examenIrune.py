
import mysql.connector
import csv
import sqlite3


class examenIrune:

# ------------- Parte 1: Listado alumnos y sus notas -------------------

    def parte1(self):

        try:
            conexion = mysql.connector.connect(user='ex2', password='adat', host='172.20.132.130', database='examen2')
            cursor = conexion.cursor()
            sql = "SELECT alumnos.APENOM, asignaturas.abreviatura,notas.nota FROM examen2.asignaturas,examen2.notas,examen2.alumnos where asignaturas.COD =notas.cod and alumnos.dni = notas.dni order by alumnos.apenom desc"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            persona = ""
            for r in resultados:
                # si es persona nueva imprimo el nombre y los guiones
                if r[0] != persona:
                    print("\n"+r[0]+"\n-----------------------------------------")
                    persona = r[0]
                print(r[1],"\t\t",r[2])
            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error -> no se ha podido establecer conexion")


# ------------- Parte 2: Modificar nombre de alumno -------------------

    def parte2(self):
        try:
            conexion = mysql.connector.connect(user='ex2', password='adat', host='172.20.132.130', database='examen2')
            dnialum = input("Escribe el DNI del alumno que deseas modificar\n")
            cursor = conexion.cursor()
            sql = "select alumnos.apenom from examen2.alumnos where alumnos.dni = "+dnialum
            cursor.execute(sql)
            resultados = cursor.fetchone()
            for r in resultados:
                print(r)

            nuevonom = input("Escribe el nuevo nombre para el alumno\n")
            sql = "update examen2.alumnos set alumnos.apenom = '" + str(nuevonom) +"' where alumnos.dni = "+dnialum
            cursor = conexion.cursor()
            cursor.execute(sql)
            print("Alumno modificado correctamente")
            print("Fin del programa.")
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error -> Ese dni no existe")
            self.parte2()



# ------------- Parte 3: Añadir/Modificar nota alumno -------------------

    def parte3(self):

        try:
            conexion = mysql.connector.connect(user='ex2', password='adat', host='172.20.132.130', database='examen2')
            dnialum = input("Escribe el DNI del alumno que quieres calificar\n")
            cursor = conexion.cursor()
            sql = "select alumnos.apenom from examen2.alumnos where alumnos.dni = " + dnialum
            cursor.execute(sql)
            resultados = cursor.fetchone()
            for r in resultados:
                print(r)
            print("Listado de asignaturas disponibles:\n")
            sql = "select * from examen2.asignaturas"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            codigos = []
            for r in resultados:
                print(r[0],"-. ",r[1]," (",r[2],")")
                codigos.append(r[0])
            elegido = -1
            while elegido not in codigos:
                elegido = int(input("Escribe el codigo de la asignatura a evaluar:\n"))

            nota = int(input("Escribe la nota del alumno:\n"))
            sql = "select count(*) from examen2.notas where notas.dni = '"+str(dnialum)+"' and notas.cod = "+str(elegido)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for r in resultados:
                if r[0] == 0:
                    estaba = False
                else:
                    estaba = True
            if estaba:
                # modificar
                sql = "update examen2.notas set notas.nota = "+ str(nota)+" where notas.dni = '"+str(dnialum)+"' and notas.cod = "+str(elegido)
                cursor.execute(sql)
                print("La nota se ha modificado.")
                conexion.commit()
            else:
                # añadir
                lista = [dnialum,elegido,nota]
                listas = [lista]
                sql = "insert into examen2.notas values (%s,%s,%s)"
                cursor.executemany(sql,list(listas))
                print("La nota se ha añadido.")
                conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print(e.__str__())
            print("Error -> no se ha podido establecer conexion")



# ------------- Parte 4: Añadir/Modificar nota alumno EXTRA -------------------

    def parte4(self):

        try:
            conexion = mysql.connector.connect(user='ex2', password='adat', host='172.20.132.130', database='examen2')
            dnialum = input("Escribe el DNI del alumno que quieres calificar\n")
            cursor = conexion.cursor(buffered=True)
            sql = "select alumnos.apenom from examen2.alumnos where alumnos.dni = " + dnialum
            cursor.execute(sql)
            resultados = cursor.fetchone()
            for r in resultados:
                print(r)
            print("Listado de asignaturas disponibles:\n")
            sql = "select * from examen2.asignaturas"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            codigos = []
            for r in resultados:
                print(r[0], "-. ", r[1], " (", r[2], ")")
                codigos.append(r[0])
            elegido = -1
            while elegido not in codigos:
                elegido = int(input("Escribe el codigo de la asignatura a evaluar:\n"))

            nota = int(input("Escribe la nota del alumno:\n"))
            cursor.execute(sql)
            cursor.callproc('insertar_nota_irune',[elegido,dnialum,nota])
            for result in cursor.stored_results():
                details = result.fetchall()
            for det in details:
                print(det)
            cursor.close()
            conexion.close()
        except Exception as e:
            print(e.__str__())
            print("Error -> no se ha podido establecer conexion")



# ------------- Menu principal -------------------
    def menu(self):


        opcion = -1
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion != 0:
            print("EXAMEN IRUNE ADAT\n\t¿Qué quieres hacer?\n")
            print("\t[1] Listado alumnos y sus notas\n")
            print("\t[2] Modificar nombre de alumno\n")
            print("\t[3] Añadir/Modificar nota alumno\n")
            print("\t[4] Añadir/Modificar nota alumno EXTRA\n")
            print("\t[0] Salir\n")
            opcion = int(input())
        if opcion == 1:
            self.parte1()
        else:
            if opcion == 2:
                self.parte2()
            else:
                if opcion ==3:
                    self.parte3()
                else:
                    if opcion == 4:
                        self.parte4()


e = examenIrune()
e.menu()