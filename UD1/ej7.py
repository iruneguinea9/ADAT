### Haz una clase llamada Persona que siga las siguientes condiciones:
# Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura.
# No queremos que se accedan directamente a ellos. Si quieres añadir algún atributo
# puedes hacerlo

import random


class Persona:
    def __init__(self, nombre = " ", edad = 0, sexo ='H',altura = 0,peso = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__sexo = sexo
        self.__altura = altura
        self.__DNI = self.__generaDNI()

    def __generaDNI(self):
       numero = random.randint(10000000,99999999)
       letra = chr(random.randint(ord('A'),ord('Z')))
       return (str)(numero)+letra

    def __str__(self):
        return "nombre: "+self.__nombre+" edad: "+(str)(self.__edad)+" DNI: "+self.__DNI

    def __get_edad(self):
        return self.__edad
    def __set_edad(self,edad):
        self.__edad=edad

    def __get_nombre(self):
        return self.__nombre

    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def __get_sexo(self):
        return self.__sexo

    def __set_sexo(self, sexo):
        self.__sexo = sexo

    def __get_peso(self):
        return self.__peso

    def __set_peso(self, peso):
        self.__peso = peso

    def __get_altura(self):
        return self.__altura

    def __set_altura(self, altura):
        self.__altura = altura

    def __get_dni(self):
        return self.__DNI

    def __set_dni(self, DNI):
        self.__DNI = DNI

    nombre = property(__get_nombre, __set_nombre)
    

pers = Persona("aaa",22)
print(pers)

