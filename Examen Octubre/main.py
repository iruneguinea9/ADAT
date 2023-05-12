# Examen ADAT Irune Guinea
import csv
from xml.etree import ElementTree as ET
from xml.dom import minidom
from Batalla import Batalla
import pickle


class main():
    # ------------------------------------------- Buscar batallas por region -------------------------------------------
    def buscar_batallas_por_region(self):
        print("BUSCAR BATALLAS POR REGIÓN\nIntroduce la región a buscar: ")
        region = input()
        existe = False  # Un booleano para saber si encuentra alguna batalla
        with open("battles.csv") as csvfile:  # Abrir CSV
            reader = csv.DictReader(csvfile)  # Un reader para leer el csv
            for row in reader:  # Leo linea a linea
                if row["region"] == region:  # Comprobar que la region es la que buscamos
                    # Estoy en la linea que me interesa

                    print("\n\tRegión: ", row["region"], "\n\tLocalizacion: ", row["location"],
                          "\n\tNombre de la batalla: ", row["name"], "\n\tAño: ", row["year"], "\n\tRey atacante: ",
                          row["attacker_king"], "\n\tRey defensor: ", row["defender_king"],
                          "\n\tResultado de la batalla: ", row["attacker_outcome"])
                    existe = True
        if not existe:
            print("No existen batallas para la region introducida")

    # -------------------------------------------- Crear XML batallas -------------------------------------------------

    def crear_XML_batallas(self):
        lista = []  # Lista donde guardo todas las batallas
        with open("battles.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lista.append(row)
        root = ET.Element("juego_tronos")  # generar raiz
        for l in lista:
            # hijos de root
            batalla = ET.Element("batalla")
            batalla.set("id", l["battle_number"])

            # hijos de batalla
            nombre = ET.Element("nombre")
            nombre.text = l["name"]

            anio = ET.Element("anio")
            anio.text = l["year"]

            region = ET.Element("region")
            region.text = l["region"]

            localizacion = ET.Element("localizacion")
            if l["location"] == "":
                localizacion.text = "no place"
            else:
                localizacion.text = l["location"]

            ataque = ET.Element("ataque")
            if l["attacker_outcome"] == "win":
                gana = 'S'
            else:
                gana = 'N'
            if l["attacker_size"] == "":
                tam = '0'
            else:
                tam = l["attacker_size"]
            ataque.set("tamanio", tam)
            ataque.set("gana",gana)

            #hijos de ataque

            rey = ET.Element("rey")
            if l["attacker_king"] == "":
                rey.text="No King"
            else:
                rey.text = l["attacker_king"]

            comandante = ET.Element("comandante")
            if l["attacker_commander"] == "":
                comandante.text="No Commander"
            else:
                comandante.text = l["attacker_commander"]

            familia = ET.Element("familia")
            familia.text =l["attacker_1"]

            ataque.append(rey)
            ataque.append(comandante)
            ataque.append(familia)

            # hay mas familias?
            if l["attacker_2"] != "":
                familia = ET.Element("familia")
                familia.text = l["attacker_2"]
                ataque.append(familia)
            if l["attacker_3"] != "":
                familia = ET.Element("familia")
                familia.text = l["attacker_3"]
                ataque.append(familia)
            if l["attacker_4"] != "":
                familia = ET.Element("familia")
                familia.text = l["attacker_4"]
                ataque.append(familia)

            # Defensa
            defensa = ET.Element("defensa")
            if l["attacker_outcome"] == "win":
                gana = 'N'
            else:
                gana = 'S'
            if l["defender_size"] == "":
                tam = '0'
            else:
                tam = l["defender_size"]

            defensa.set("tamanio", tam)
            defensa.set("gana", gana)

            # hijos de defensa

            rey = ET.Element("rey")
            if l["defender_king"] == "":
                rey.text = "No King"
            else:
                rey.text = l["defender_king"]

            comandante = ET.Element("comandante")
            if l["defender_commander"] == "":
                comandante.text="No Commander"
            else:
                comandante.text = l["defender_commander"]

            familia = ET.Element("familia")
            familia.text = l["defender_1"]

            defensa.append(rey)
            defensa.append(comandante)
            defensa.append(familia)

            # hay mas familias?
            if l["defender_2"] != "":
                familia = ET.Element("familia")
                familia.text = l["defender_2"]
                defensa.append(familia)
            if l["defender_3"] != "":
                familia = ET.Element("familia")
                familia.text = l["defender_3"]
                defensa.append(familia)
            if l["defender_4"] != "":
                familia = ET.Element("familia")
                familia.text = l["defender_4"]
                defensa.append(familia)

            batalla.append(nombre)
            batalla.append(anio)
            batalla.append(region)
            batalla.append(localizacion)
            batalla.append(ataque)
            batalla.append(defensa)

            root.append(batalla)
            str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
            f = open("battles.xml", "w")
            f.write(str)
            f.close()

    # ------------------------------------- Crear fichero binario de objetos -------------------------------------------

    def crearFicheroBatalla(self):
        with open("battles.bin", "wb") as f:
            raiz = ET.parse("battles.xml").getroot()
            lista = raiz.findall("batalla")
            for bt in lista:
                nombre = bt.find("nombre")
                region = bt.find("region")
                id = bt.get("id")
                anio = bt.find("anio")
                localizacion = bt.find("localizacion")
                ataque = bt.find("ataque")
                rey_atacante = ataque.findtext("rey")
                gana_atacante = ataque.get("gana")
                defensa = bt.find("defensa")
                rey_defensor = defensa.findtext("rey")

                batalla = Batalla(id,nombre.text,anio.text,region.text,localizacion.text,rey_atacante,rey_defensor,gana_atacante)
                pickle.dump(batalla, f)
        f.close()
        print("FICHERO CREADO")

    # --------------------------------- Eliminar batalla del fichero ---------------------------------------------------
    def eliminarBatallaFichero(self):
        idborrar = input("Introduce el identificador de la batalla a eliminar: ")
        lista = []
        borraAlguna = False
        with open("battles.bin", "rb") as f:
            while True:
                try:
                    batalla = pickle.load(f)
                    if batalla.id != idborrar:
                        lista.append(batalla)
                    else:
                        print("CUIDADO!\nSeguro que quieres borrar esta batalla? ")
                        batalla.__str__()
                        res = input("s/n?")
                        while res != 's' and res != 'n':
                            print("Valor incorrecto, quieres borrar la batalla? s/n")
                            res = input("s/n?")
                        if res == 's':
                            borraAlguna = True
                        else:
                            break
                except EOFError:
                    break
        if (borraAlguna):
            with open("battles.bin", "wb") as f:
                for l in lista:
                    pickle.dump(l, f)
            print("Batalla borrada")
        else:
            print("No se ha borrado ninguna batalla")

    # ------------------------------------------------- Menú -----------------------------------------------------------
    def menu(self):
        print("JUEGO DE TRONOS\n¿Que quieres hacer?")
        print(
            "\n\t[1] Buscar batallas por región.\n\t[2] Crear XML batallas.\n\t[3] Crear fichero binario objetos.\n\t[4] Eliminar batalla fic. Binario objetos\n\n\t[0] Salir")
        opcion = int(input())

        while (opcion < 0 or opcion > 4):
            print("Opcion incorrecta, introduce otra opcion: ")
            opcion = int(input())
        while (True):
            if opcion == 1:
                self.buscar_batallas_por_region()  # para probar usar The Riverlands
            elif opcion == 2:
                self.crear_XML_batallas()
            elif opcion == 3:
                self.crearFicheroBatalla()
            elif opcion == 4:
                self.eliminarBatallaFichero()
            elif opcion == 0:
                exit(0)
            self.menu()


pruebas = main()
pruebas.menu()

# para hacer pruebas
# with open("battles.bin","rb") as f:
#     while True:
#         try:
#             batalla = pickle.load(f)
#             batalla.__str__()
#
#         except EOFError:
#             break;
