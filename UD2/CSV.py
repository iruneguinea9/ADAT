import csv

class CSV:
    def mostrarAtletas(self):
        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            cont = 0
            olimpiadas = []
            for row in reader:
                if not row["Games"] in olimpiadas:
                    print(row["Games"])
                    cont += 1
                    olimpiadas.append(row["Games"])

            print(cont)

    def crearCsvOlimpiadas(self):
        olimpiadas = []
        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            with open("olimpiadas.csv",'w') as csvolimpiadas:
                columnas = ["Games","Year","Season","City"]
                writer = csv.DictWriter(csvolimpiadas,columnas)
                writer.writeheader()
                for row in reader:
                    if not row["Games"] in olimpiadas:
                        olimpiadas.append(row["Games"])
                        writer.writerow({columnas[0]:row["Games"],columnas[1]:row["Year"],columnas[2]:row["Season"],columnas[3]:row["City"]})

    def buscarDeportista(self):
        cadena = input("Introduce la cadena para buscar")
        yaEstan = []
        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if cadena in row["Name"]:
                    if not row["Name"] in yaEstan:
                        yaEstan.append(row["Name"])
                        print("Deportista:" ,row["Name"])
                        print("\tId: ",row["ID"]," Sex: ",row["Sex"]," Age: ",row["Age"]," Height: ",row["Height"]," Weight: ",row["Weight"]," Team: ",row["Team"]," NOC: ",row["NOC"])
                    print("\t Games: ", row["Games"], " Year: ", row["Year"], " Season: ", row["Season"], " City: ",
                          row["City"], " Sport", row["Sport"], " Event: ", row["Event"], " Medal: ", row["Medal"])
            if len(yaEstan) == 0:
                print("No hay deportistas con esa cadena en el nombre")

    def buscarDeporteOlimpiada(self):
        sport = input("Introduce el deporte ")
        year = input("Introduce el año ")
        season = input("Introduce la temporada ")
        contador = 0
        primera = True
        with open("athlete_events.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if primera:
                    print("[EDICION OLIMPICA] Deporte: ", sport, " Games: ", row["Games"], " City: ", row["City"])
                    primera = False
                if row["Sport"] == sport and row["Year"] == year and row["Season"] == season:
                    print("\t Nombre: ",row["Name"]," Evento: ",row["Event"], " Medalla: ",row["Medal"])
                    contador += 1
            if(contador==0):
                print("No se han encontrado deportistas en la edicion")




c = CSV()
#c.crearCsvOlimpiadas()
#c.buscarDeportista()
c.buscarDeporteOlimpiada()
