
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Olimpiada, Evento, Deporte, Deportista, Participacion, Equipo


class olimpiadasAlchemy:

    # ------------- Crear engine MYSQL -------------------
    def crearEngineMYSQL(self):

        try:
            engine = create_engine("mysql+pymysql://admin:password@localhost/olimpiadas", echo=False)
            return engine
        except Exception as ex1:
            print("Error -> no se ha podido establecer conexion")


    # ------------- Crear engine SQLite -------------------
    def crearEngineSQLite(self):

        try:
            engine = create_engine('sqlite:///embebido.db', echo=False)

            return engine
        except Exception as ex1:
            print("Error -> no se ha podido establecer conexion")

    # ------------- Listar deportistas en diferentes deportes-------------------

    def listardeportistas(self,sesion):

        # --------------- Elegir temporada -----------------
        temporada = 'P'
        while temporada != 'S' and temporada != 'W':
            temporada = input("Que temporada?(W/S)").upper()
        if temporada == 'S':
            temporada = 'Summer'
        else:
            temporada = 'Winter'

        # --------------- Enseñar ediciones ----------------
        entra = False
        olimpiadas = []
        for olimp in sesion.query(Olimpiada).filter(Olimpiada.temporada == temporada).all():
            print("\tid: " + str(olimp.id_olimpiada) + " año: " + str(olimp.anio) + " ciudad: " + str(olimp.ciudad))
            olimpiadas.append(str(olimp.id_olimpiada))
            entra = True
        if(entra):
            idolimpiada = input("Introduce el id de una olimpiada: ")
            while idolimpiada not in olimpiadas:
                idolimpiada = input("Introduce un id correcto: ")

            # --------------- Elegir deporte ----------------
            print("Deportes de la olimpiada " + idolimpiada + ":")
            olimpiada = sesion.query(Olimpiada).get(idolimpiada)
            deportes = []
            for evento in olimpiada.eventos:
                if evento.deporte not in deportes:
                    deportes.append(evento.deporte)

            ids = []
            for deporte in deportes:
                print("\tid: " + str(deporte.id_deporte) + " deporte: " + deporte.nombre)
                ids.append(str(deporte.id_deporte))
            iddeporte = input("Introduce el id de un deporte: ")
            while iddeporte not in ids:
                iddeporte = input("Introduce un id válido: ")

            # --------------- Elegir evento ----------------
            print("Eventos del deporte " + iddeporte + " en la olimpiada " + idolimpiada + ":")
            idsev = []
            for evento in sesion.query(Evento).filter(Evento.id_olimpiada == idolimpiada, Evento.id_deporte == iddeporte):
                print("\tid: " + str(evento.id_evento) + " nombre: " + str(evento.nombre))
                idsev.append(str(evento.id_evento))
            idevento = input("Introduce el id de un evento: ")
            while idevento not in idsev:
                idevento = input("Introduce un id válido: ")

            # --------------- visualizar ----------------

            # --------------- info de la seleccion ----------------
            self.visualizarinfo(temporada,idolimpiada,iddeporte,idevento,sesion)
            # --------------- info de cada deportista ----------------
            self.visualizardeportistas(sesion,idevento)
        else:
            print("No hay ninguna olimpiada en esta temporada")

    # ------------- Visualizar info -----------------
    def visualizarinfo(self,temporada,idol,iddep,idev,sesion):
        for olimpiada in sesion.query(Olimpiada).filter(Olimpiada.id_olimpiada == idol):
            ol = olimpiada.nombre
        for deporte in sesion.query(Deporte).filter(Deporte.id_deporte == iddep):
            dep = deporte.nombre
        for evento in sesion.query(Evento).filter(Evento.id_evento == idev):
            ev = evento.nombre
        print("\n\tTemporada: ",temporada,"\n\tEdicion: ",ol,"\n\tDeporte: ",dep,"\n\tEvento: ",ev)

    # ------------- Visualizar deportistas -----------------
    def visualizardeportistas(self, sesion,idevento):
        for participacion in sesion.query(Participacion).filter(Participacion.id_evento == idevento):
            for deportista in sesion.query(Deportista).filter(Deportista.id_deportista == participacion.id_deportista):
                print("\nDeportista: ",deportista.nombre," Altura: ",deportista.altura," Peso: ",deportista.peso," Edad: ",participacion.edad,"Equipo: ",self.queEquipoEs(participacion.id_equipo,sesion)," Medalla: ",participacion.medalla)

    # ------------- que equipo es -----------------

    def queEquipoEs(self,id,sesion):
        for equipo in sesion.query(Equipo).filter(Equipo.id_equipo == id):
            nombre = equipo.nombre
        return nombre

    # ------------- Ejercicio 1 -------------------

    def parte1(self):
        opcion = -1
        while opcion != 1 and opcion != 2:
            opcion = int(input("Listado de deportistas\n¿Que base quieres usar?\n\n\t[1]MySQL\n\t[2]SQLite\n"))
        if opcion == 1:
            # MySQL
            db = self.crearEngineMYSQL()
        else:
            # SQLite
            db = self.crearEngineSQLite()
        Session = sessionmaker(bind=db)
        sesion = Session()
        self.listardeportistas(sesion)

    # ------------- Modificar medalla -------------------
    def modificarMedalla(self,sesion):
        filtro = input("Introduce el filtro para buscar al deportista: ")
        # ------------- Buscar deportista -------------------
        deportistas = []
        participaciones = []
        indice = 1
        for deportista in sesion.query(Deportista).filter(Deportista.nombre.like("%" + filtro + "%")):
            deportistas.append(deportista.id_deportista)
            print(deportista.id_deportista," ",deportista.nombre)
        # egiaztatu ea dagoen batenbat
        elegido = -1
        while elegido not in deportistas:
            elegido = int(input("De que deportista deseas modificar la medalla?"))


        # ------------- Seleccionar participacion -------------------

        for participacion in sesion.query(Participacion).filter(Participacion.id_deportista == elegido):
            print("\tCodigo: ", indice, " Evento:", self.queEventoEs(sesion,participacion.id_evento), " celebrado en ", self.queEventoDonde(sesion,participacion.id_evento))
            indice+=1
            participaciones.append(participacion)
        elegida = -1
        while elegida < 1 or elegida > indice:
            elegida = int(input("De que participacion deseas modificar la medalla?"))
        cualParti = participaciones[elegida-1]
        cualMedalla = -1
        while cualMedalla <1 or cualMedalla>4:
            cualMedalla= int(input("Que medalla quieres poner? \n\t[1] Gold\n\t[2] Silver\n\t[3] Bronze\n\t[4] NA\n"))
        if cualMedalla==1:
            nuevaMedalla = 'Gold'
        else:
            if cualMedalla == 2:
                nuevaMedalla = 'Silver'
            else:
                if cualMedalla == 3:
                    nuevaMedalla = 'Bronze'
                else:
                    nuevaMedalla = 'NA'
        cualParti.medalla = nuevaMedalla
        sesion.commit()
        db = self.crearEngineSQLite()
        Session = sessionmaker(bind=db)
        sesion = Session()
        sesion.execute("PRAGMA foreign_keys = 1")
        partiNueva = sesion.query(Participacion).filter(Participacion.id_deportista == cualParti.id_deportista, Participacion.id_evento == cualParti.id_evento).one()
        partiNueva.medalla = nuevaMedalla
        sesion.commit()
    # ------------- que evento es -------------------
    def queEventoEs(self,sesion,id):
        for evento in sesion.query(Evento).filter(Evento.id_evento == id):
            nombre = evento.nombre
        return nombre

    # ------------- que evento donde -------------------
    def queEventoDonde(self, sesion, id):
        for evento in sesion.query(Evento).filter(Evento.id_evento == id):
            ol = evento.id_olimpiada
        for olimpiada in sesion.query(Olimpiada).filter(Olimpiada.id_olimpiada == ol):
            donde = olimpiada.nombre
        return donde
    # ------------- Ejercicio 2 -------------------

    def parte2(self):

        db = self.crearEngineMYSQL()
        Session = sessionmaker(bind=db)
        sesion = Session()
        self.modificarMedalla(sesion)


    # ------------- aniadir Deportista / Participacion -------------------
    def aniadirDepPart(self,sesion):
        filtro = input("Introduce el filtro para buscar al deportista: ")
        # ------------- Buscar deportista -------------------
        deportistas = []
        existe = False
        indice = 1
        for deportista in sesion.query(Deportista).filter(Deportista.nombre.like("%" + filtro + "%")):
            deportistas.append(deportista)
            print(indice," ",deportista.nombre)
            indice += 1
            existe = True
        if existe:
            # cual?
            elegido = -1
            while elegido <1 or elegido >indice:
                elegido = int(input("Que deportista es?"))
            deportista2 = deportistas[elegido-1]

        else:
            # crear uno nuevo
            print("No existe deportista con esas caracteristicas, se creara uno nuevo")
            nombre = input("Cual es el nombre del deportista?")
            sexo = input("Cual es el sexo del deportista?")
            peso = int(input("Cual es el peso del deportista?"))
            altura = int(input("Cual es la altura del deportista?"))
            deportista = Deportista(nombre=nombre, sexo=sexo, peso=peso, altura=altura)
            sesion.add(deportista)
            sesion.commit()
            # meterlo a SQLite
            db = self.crearEngineSQLite()
            Session = sessionmaker(bind=db)
            sesion = Session()
            sesion.execute("PRAGMA foreign_keys = 1")
            deportista2 = Deportista(nombre=nombre, sexo=sexo, peso=peso, altura=altura)
            sesion.add(deportista2)
            sesion.commit()
        db = self.crearEngineMYSQL()
        Session = sessionmaker(bind=db)
        sesion = Session()
        # --------------- Elegir temporada -----------------
        temporada = 'P'
        while temporada != 'S' and temporada != 'W':
            temporada = input("Que temporada?(W/S)").upper()
        if temporada == 'S':
            temporada = 'Summer'
        else:
            temporada = 'Winter'

        # --------------- Enseñar ediciones ----------------
        entra = False
        olimpiadas = []
        for olimp in sesion.query(Olimpiada).filter(Olimpiada.temporada == temporada).all():
            print("\tid: " + str(olimp.id_olimpiada) + " año: " + str(olimp.anio) + " ciudad: " + str(
                olimp.ciudad))
            olimpiadas.append(str(olimp.id_olimpiada))
            entra = True
        if (entra):
            idolimpiada = input("Introduce el id de una olimpiada: ")
            while idolimpiada not in olimpiadas:
                idolimpiada = input("Introduce un id correcto: ")

            # --------------- Elegir deporte ----------------
            print("Deportes de la olimpiada " + idolimpiada + ":")
            olimpiada = sesion.query(Olimpiada).get(idolimpiada)
            deportes = []
            for evento in olimpiada.eventos:
                if evento.deporte not in deportes:
                    deportes.append(evento.deporte)

            ids = []
            for deporte in deportes:
                print("\tid: " + str(deporte.id_deporte) + " deporte: " + deporte.nombre)
                ids.append(str(deporte.id_deporte))
            iddeporte = input("Introduce el id de un deporte: ")
            while iddeporte not in ids:
                iddeporte = input("Introduce un id válido: ")

            # --------------- Elegir evento ----------------
            print("Eventos del deporte " + iddeporte + " en la olimpiada " + idolimpiada + ":")
            idsev = []
            for evento in sesion.query(Evento).filter(Evento.id_olimpiada == idolimpiada, Evento.id_deporte == iddeporte):
                print("\tid: " + str(evento.id_evento) + " nombre: " + str(evento.nombre))
                idsev.append(str(evento.id_evento))
            idevento = input("Introduce el id de un evento: ")
            while idevento not in idsev:
                idevento = input("Introduce un id válido: ")
            idseq = []
            for equipo in sesion.query(Equipo).all():
                print("\tid: " + str(equipo.id_equipo) + " nombre: " + str(equipo.nombre))
                idseq.append(str(equipo.id_equipo))
            idequipo = input("Introduce el id del equipo: ")
            while idequipo not in idseq:
                idequipo = input("Introduce un id válido: ")
            edad = int(input("Introduce la edad"))
            cualMedalla = -1
            while cualMedalla < 1 or cualMedalla > 4:
                cualMedalla = int(
                    input("Que medalla quieres poner? \n\t[1] Gold\n\t[2] Silver\n\t[3] Bronze\n\t[4] NA\n"))
            if cualMedalla == 1:
                nuevaMedalla = 'Gold'
            else:
                if cualMedalla == 2:
                    nuevaMedalla = 'Silver'
                else:
                    if cualMedalla == 3:
                        nuevaMedalla = 'Bronze'
                    else:
                        nuevaMedalla = 'NA'
            # ------------- Crear participacion -------------------
            nuevaParticipacion = Participacion(id_deportista =deportista.id_deportista,id_evento= int(idevento),id_equipo = int(idequipo),edad=edad,medalla=nuevaMedalla)
            # meterlo a MYSQL
            nombreDepor = deportista.nombre
            print(nuevaParticipacion.id_deportista)
            sesion.add(nuevaParticipacion)
            sesion.commit()
            # meterlo a SQLite
            db = self.crearEngineSQLite()
            Session = sessionmaker(bind=db)
            sesion = Session()
            sesion.execute("PRAGMA foreign_keys = 1")
            deportistaNuevo = sesion.query(Deportista).where(Deportista.nombre==nombreDepor).one()
            nuevaParticipacion2 = Participacion(id_deportista =deportistaNuevo.id_deportista,id_evento= int(idevento),id_equipo = int(idequipo),edad=edad,medalla=nuevaMedalla)
            sesion.add(nuevaParticipacion2)
            sesion.commit()


    # ------------- Crear deportista -------------------
    def crearDeportista(self):
        nombre = input("Cual es el nombre del deportista?")
        sexo = input("Cual es el sexo del deportista?").upper()
        peso = int(input("Cual es el peso del deportista?"))
        altura = int(input("Cual es la altura del deportista?"))
        nuevoDeportista = Deportista(nombre=nombre, sexo=sexo, peso=peso, altura=altura)
        # meterlo a MYSQL
        db = self.crearEngineMYSQL()
        Session = sessionmaker(bind=db)
        sesion = Session()
        sesion.add(nuevoDeportista)
        sesion.commit()
        # meterlo a SQLite
        db = self.crearEngineSQLite()
        Session = sessionmaker(bind=db)
        sesion = Session()
        sesion.execute("PRAGMA foreign_keys = 1")
        nuevoDeportista2 = Deportista(nombre=nombre, sexo=sexo, peso=peso, altura=altura)

        sesion.add(nuevoDeportista2)
        sesion.commit()
        return nuevoDeportista

    # ------------- Ejercicio 3 -------------------

    def parte3(self):
        db = self.crearEngineMYSQL()
        Session = sessionmaker(bind=db)
        sesion = Session()
        self.aniadirDepPart(sesion)

    # ------------- eliminar participacion  -------------------

    def eliminarParticipacion(self,sesion):
        filtro = input("Introduce el filtro para buscar al deportista: ")
        # ------------- Buscar deportista -------------------
        deportistas = []
        participaciones = []
        indice = 1
        for deportista in sesion.query(Deportista).filter(Deportista.nombre.like("%" + filtro + "%")):
            deportistas.append(deportista.id_deportista)
            print(deportista.id_deportista," ",deportista.nombre)
        # egiaztatu ea dagoen batenbat
        elegido = -1
        while elegido not in deportistas:
            elegido = int(input("Que deportista?"))


        # ------------- Seleccionar participacion -------------------
        cuantas = 0
        for participacion in sesion.query(Participacion).filter(Participacion.id_deportista == elegido):
            print("\tCodigo: ", indice, " Evento:", self.queEventoEs(sesion,participacion.id_evento), " celebrado en ", self.queEventoDonde(sesion,participacion.id_evento))
            participaciones.append(participacion)
            cuantas += 1
        elegida = -1
        while elegida < 1 or elegida > indice:
            elegida = int(input("Que evento quieres borrar?"))
        cualParti = participaciones[elegida-1]
        if cuantas > 1:
            # tiene mas de una participacion
            sesion.delete(cualParti)
            print("PARTICIPACION BORRADA DE MYSQL")
        else:
            # hay que borrar el deportista
            deportista = cualParti.deportista
            sesion.delete(cualParti)
            sesion.delete(deportista)
            print("PARTICIPACION Y DEPORTISTAS BORRADOS DE MYSQL")
        sesion.commit()
        db = self.crearEngineSQLite()
        Session = sessionmaker(bind=db)
        sesion = Session()
        sesion.execute("PRAGMA foreign_keys = 1")
        cuantas = 0
        participaciones2 = []
        deportistaID = sesion.query(Deportista).filter(Deportista.nombre==deportista.nombre).one()
        for participacion in sesion.query(Participacion).filter(Participacion.id_deportista ==deportistaID.id_deportista):
            participaciones2.append(participacion)
            cuantas += 1

        cualParti2 = participaciones2[elegida - 1]
        if cuantas > 1:
            # tiene mas de una participacion
            sesion.delete(cualParti2)
            print("PARTICIPACION BORRADA DE SQLITE")
        else:
            # hay que borrar el deportista
            deportista2 = cualParti2.deportista
            sesion.delete(cualParti2)
            sesion.delete(deportista2)
            print("PARTICIPACION Y DEPORTISTAS BORRADOS DE SQLITE")

        sesion.commit()
    # ------------- Ejercicio 4 -------------------

    def parte4(self):
        db = self.crearEngineMYSQL()
        Session = sessionmaker(bind=db)
        sesion = Session()
        self.eliminarParticipacion(sesion)

    # ------------- Menu principal -------------------
    def menu(self):
        opcion = -1
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion != 0:
            print("OLIMPIADAS ALCHEMY BD\n\t¿Qué quieres hacer?\n")
            print("\t[1] Listado de deportistas participantes\n")
            print("\t[2] Modificar medalla deportista\n")
            print("\t[3] Añadir deportista/participación\n")
            print("\t[4] Eliminar participación\n")
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
                    self.parte3()
                    self.menu()
                else:
                    if opcion == 4:
                        self.parte4()
                        self.menu()



o = olimpiadasAlchemy()
o.menu()