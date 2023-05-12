from builtins import print

import mysql.connector
import csv
import sqlite3

class olimpiadasDB:

    # -----------MYSQL-------------
    def crearConexionMYSQL(self):

        try:
            conDB = mysql.connector.connect(user='admin', password='password', host='localhost')
            # cursor para ejecutar consulta
            cursor = conDB.cursor()
            with open("olimpiadas.sql") as f:
                sql = f.read()
                resultados = cursor.execute(sql, multi=True)
            for r in resultados:
                print(r)
            # cerrar cursor
            cursor.close()
            # cerrar conexion
            conDB.close()
        except Exception as ex1:
            print("Error -> no se ha podido establecer conexion")

    # -----------MYSQL-------------
    def llenarBaseMYSQL(self):
        # Crear diccionarios
        dicDeportistas ={}
        dicOlimpiadas = {}
        dicEventos = {}
        dicEquipo = {}
        dicDeportes = {}
        dicParticipaciones = {}
        id_equipo = 1
        id_deporte = 1
        id_olimpiada = 1
        id_evento = 1
        cont = 0
        try:
            ruta = input("introduce el nombre del csv de informacion") #"athlete_events_recortado.csv"
            with open(ruta) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cont += 1
                    if row["Team"] not in dicEquipo.keys():
                        dicEquipo[row["Team"]] = [id_equipo,row["Team"],row["NOC"]]
                        id_eq_actual = id_equipo
                        id_equipo += 1
                    else:
                        id_eq_actual = dicEquipo[row["Team"]][0]
                    if row["ID"] not in dicDeportistas.keys():
                        if row["Weight"] == "NA":
                            peso = 0
                        else:
                            peso = row["Weight"]
                        if row["Height"] == "NA":
                            altura = 0
                        else:
                            altura = row["Height"]
                        dicDeportistas[row["Name"]] = [int(row["ID"]),row["Name"],row["Sex"],peso,altura]
                    if(row["Sport"]) not in dicDeportes.keys():
                        dicDeportes[row["Sport"]] = [id_deporte,row["Sport"]]
                        id_dep_actual = id_deporte
                        id_deporte += 1
                    else:
                        id_dep_actual = dicDeportes[row["Sport"]][0]
                    if(row["Games"]) not in dicOlimpiadas.keys():
                        dicOlimpiadas[row["Games"]] = [id_olimpiada,row["Games"],row["Year"],row["Season"],row["City"]]
                        id_ol_actual = id_olimpiada
                        id_olimpiada += 1
                    else:
                        id_ol_actual = dicOlimpiadas[row["Games"]][0]
                    clave = row["Event"]+str(id_ol_actual);
                    if clave not in dicEventos.keys():
                        dicEventos[clave] = [id_evento,row["Event"],id_ol_actual,id_dep_actual]
                        id_ev_actual = id_evento
                        id_evento += 1
                    else:
                        id_ev_actual = dicEventos[row["Event"]+str(id_ol_actual)][0]
                    dicParticipaciones[cont] = [int(row["ID"]),id_ev_actual,id_eq_actual,row["Age"],row["Medal"]]
        except Exception as e:
            print("El archivo csv no existe")
            self.borrarDatosMYSQL()
        # LLenar tablas
        try:
            conn = mysql.connector.connect(user='admin', password='password',
                                           host='localhost',
                                           database='olimpiadas')
            # cursor para ejecutar consulta
            cursor = conn.cursor()
            sql = "INSERT INTO `olimpiadas`.`Equipo` (`id_equipo`, `nombre`, `iniciales`) VALUES  (%s,%s,%s);"
            cursor.executemany(sql,list(dicEquipo.values()))
            sql = "INSERT INTO `olimpiadas`.`Deportista` (`id_deportista`, `nombre`, `sexo`, `peso`, `altura`) VALUES  (%s,%s,%s,%s,%s);"
            cursor.executemany(sql, list(dicDeportistas.values()))
            sql = "INSERT INTO `olimpiadas`.`Deporte` (`id_deporte`, `nombre`) VALUES  (%s,%s);"
            cursor.executemany(sql, list(dicDeportes.values()))
            sql = "INSERT INTO `olimpiadas`.`Olimpiada` (`id_olimpiada`, `nombre`, `anio`, `temporada`, `ciudad`)  VALUES  (%s,%s,%s,%s,%s);"
            cursor.executemany(sql, list(dicOlimpiadas.values()))
            sql = "INSERT INTO `olimpiadas`.`Evento` (`id_evento`, `nombre`, `id_olimpiada`, `id_deporte`) VALUES (%s,%s,%s,%s);"
            cursor.executemany(sql, list(dicEventos.values()))
            conn.commit()
            sql = "INSERT INTO olimpiadas.Participacion (id_deportista, id_evento, id_equipo, edad, medalla) VALUES (%s,%s,%s,%s,%s);"
            cursor.executemany(sql, list(dicParticipaciones.values()))
            conn.commit()
            cursor.close()
            conn.close()
            print("La carga se ha realizado correctamente")
        except Exception as e:
            print("Error -> Ha ocurrido algun error en la carga")
            self.borrarDatosMYSQL()

    # -----------MYSQL-------------
    def borrarDatosMYSQL(self):
        conn = mysql.connector.connect(user='admin', password='password',
                                       host='localhost',
                                       database='olimpiadas')
        try:
            # cursor para ejecutar consulta
            cursor = conn.cursor()
            sql = "Delete from olimpiadas.Participacion"
            cursor.execute(sql)
            sql = "Delete from olimpiadas.Evento"
            cursor.execute(sql)
            sql = "Delete from olimpiadas.Olimpiada"
            cursor.execute(sql)
            sql = "Delete from olimpiadas.Equipo"
            cursor.execute(sql)
            sql = "Delete from olimpiadas.Deportista"
            cursor.execute(sql)
            sql = "Delete from olimpiadas.Deporte"
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error -> al borrar de las tablas")

    def parte1(self):
            self.crearConexionMYSQL()
            self.borrarDatosMYSQL()
            self.llenarBaseMYSQL()

    def borrarDatosSQLite(self):
        conexion = sqlite3.connect("embebido.db")
        cursor = conexion.cursor()
        try:
            # cursor para ejecutar consulta
            cursor = conexion.cursor()
            sql = "Delete from Participacion"
            cursor.execute(sql)
            sql = "Delete from Evento"
            cursor.execute(sql)
            sql = "Delete from Olimpiada"
            cursor.execute(sql)
            sql = "Delete from Equipo"
            cursor.execute(sql)
            sql = "Delete from Deportista"
            cursor.execute(sql)
            sql = "Delete from Deporte"
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("Error -> al borrar de las tablas")
    def llenarBaseSQLite(self):
        # Crear diccionarios
        dicDeportistas = {}
        dicOlimpiadas = {}
        dicEventos = {}
        dicEquipo = {}
        dicDeportes = {}
        dicParticipaciones = {}
        id_equipo = 1
        id_deporte = 1
        id_olimpiada = 1
        id_evento = 1
        cont = 0
        try:
            # ruta = input("introduce el nombre del csv de informacion")  # "athlete_events_recortado.csv"
            # with open(ruta) as csvfile:
            with open("athlete_events_recortado.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cont += 1
                    if row["Team"] not in dicEquipo.keys():
                        dicEquipo[row["Team"]] = [id_equipo, row["Team"], row["NOC"]]
                        id_eq_actual = id_equipo
                        id_equipo += 1
                    else:
                        id_eq_actual = dicEquipo[row["Team"]][0]
                    if row["ID"] not in dicDeportistas.keys():
                        if row["Weight"] == "NA":
                            peso = 0
                        else:
                            peso = row["Weight"]
                        if row["Height"] == "NA":
                            altura = 0
                        else:
                            altura = row["Height"]
                        dicDeportistas[row["Name"]] = [int(row["ID"]), row["Name"], row["Sex"], peso, altura]
                    if (row["Sport"]) not in dicDeportes.keys():
                        dicDeportes[row["Sport"]] = [id_deporte, row["Sport"]]
                        id_dep_actual = id_deporte
                        id_deporte += 1
                    else:
                        id_dep_actual = dicDeportes[row["Sport"]][0]
                    if (row["Games"]) not in dicOlimpiadas.keys():
                        dicOlimpiadas[row["Games"]] = [id_olimpiada, row["Games"], row["Year"], row["Season"],
                                                       row["City"]]
                        id_ol_actual = id_olimpiada
                        id_olimpiada += 1
                    else:
                        id_ol_actual = dicOlimpiadas[row["Games"]][0]
                    clave = row["Event"] + str(id_ol_actual);
                    if clave not in dicEventos.keys():
                        dicEventos[clave] = [id_evento, row["Event"], id_ol_actual, id_dep_actual]
                        id_ev_actual = id_evento
                        id_evento += 1
                    else:
                        id_ev_actual = dicEventos[row["Event"] + str(id_ol_actual)][0]
                    dicParticipaciones[cont] = [int(row["ID"]), id_ev_actual, id_eq_actual, row["Age"], row["Medal"]]
        except Exception as e:
            print("El archivo csv no existe")
            self.borrarDatosSQLite()
            # LLenar tablas
        try:
            conexion = sqlite3.connect("embebido.db")
            cursor = conexion.cursor()

            sql = "INSERT INTO Equipo (id_equipo, nombre, iniciales) VALUES  (?,?,?);"
            print("1")
            cursor.executemany(sql, list(dicEquipo.values()))
            print("2")
            sql = "INSERT INTO Deportista (id_deportista, nombre, sexo, peso, altura) VALUES  (?,?,?,?,?);"
            cursor.executemany(sql, list(dicDeportistas.values()))
            sql = "INSERT INTO Deporte (id_deporte, nombre) VALUES  (?,?);"
            cursor.executemany(sql, list(dicDeportes.values()))
            sql = "INSERT INTO Olimpiada (id_olimpiada, nombre, anio, temporada, ciudad)  VALUES  (?,?,?,?,?);"
            cursor.executemany(sql, list(dicOlimpiadas.values()))
            sql = "INSERT INTO Evento (id_evento, nombre, id_olimpiada, id_deporte) VALUES (?,?,?,?);"
            cursor.executemany(sql, list(dicEventos.values()))
            conexion.commit()
            sql = "INSERT INTO Participacion (id_deportista, id_evento, id_equipo, edad, medalla) VALUES (?,?,?,?,?);"
            cursor.executemany(sql, list(dicParticipaciones.values()))
            conexion.commit()
            cursor.close()
            conexion.close()
            print("La carga se ha realizado correctamente")
        except Exception as e:
            print("Error -> Ha ocurrido algun error en la carga")
            self.borrarDatosSQLite()

    def crearConexionSQLite(self):
        conexion = sqlite3.connect("embebido.db")
        cursor = conexion.cursor()
        with open("olimpiadas.db.sql") as f:
            cursor.executescript(f.read())
        cursor.close()
        conexion.close()
    def consultarEmbebido(self):
        conexion = sqlite3.connect("embebido.db")
        cursor = conexion.cursor()
        sql = "select nombre from Equipo"
        resultados = cursor.execute(sql)
        for r in resultados:
            print(r)
        cursor.close()
        conexion.close()
    def parte2(self):
        self.crearConexionSQLite()
        self.llenarBaseSQLite()

    def menu(self):
        opcion = -1
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion !=4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion!=0:
            print("OLIMPIADAS BD\n\t¿Qué quieres hacer?\n")
            print("\t[1] Crear BBDD MySQL\n")
            print("\t[2] Crear BBDD SQLite\n")  # mantener orden
            print("\t[3] Listado de deportistas en diferentes deportes\n")
            print("\t[4] Listado de deportistas principiantes\n")
            print("\t[5] Modificar medalla deportista\n")
            print("\t[6] Añadir deportista/participacion\n")
            print("\t[7] Eliminar participacion\n")
            print("\t[0] Salir\n")
            opcion = int(input())
        if opcion == 1:
            self.parte1()
            self.menu()
        else:
            if opcion == 2:
                self.parte2()
                self.menu()
            else:
                if opcion == 3:
                    self.consultarEmbebido()





o = olimpiadasDB()
o.menu()
