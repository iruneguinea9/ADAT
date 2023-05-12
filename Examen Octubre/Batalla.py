class Batalla():

    def __init__(self,id,nombre,anio,region,localizacion,rey_atacante,rey_defensor,gana_atacante):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.region = region
        self.localizacion = localizacion
        self.rey_atacante = rey_atacante
        self.rey_defensor = rey_defensor
        self.gana_atacante = gana_atacante

    def __str__(self):
        if self.gana_atacante=="S":
            gana = "win"
        else:
            gana = "loose"
        print("The ",self.nombre," took place in ",self.region," in the year ",self.anio,". The King(s) ",self.rey_atacante," fought against ",self.rey_defensor," and he/they ",gana)