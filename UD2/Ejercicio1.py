## Sistema de archivos
## Irune Guinea Zufiaurre
# Menú
import shutil,os

class ejercicio_menu:

    def creardir(self):
        ruta = input("Introduce el nombre de la ruta")
        nombre = input("Introduce el nombre del directorio a crear")
        ## comprobar que la ruta es correcta
        if not os.path.exists(ruta):
            print("ERROR\nLa ruta introducida no existe")
        else:
            os.mkdir(os.path.join(ruta,nombre))
            print("Se ha creado el directorio")

    def listardir(self):
        ruta = input("Introduce el nombre de la ruta")
        ## comprobar que la ruta es correcta
        if not os.path.exists(ruta):
            print("ERROR\nLa ruta introducida no existe")
        else:
            lista = os.listdir(ruta)
            listadirectorios = []
            listaarchivos = []
            for i in lista:
                if os.path.isdir(i):
                    listadirectorios.append(i)
                else:
                    listaarchivos.append(i)
            print("Directorios: ")
            print(listadirectorios)
            print("Archivos: ")
            print(listaarchivos)
    def copiar(self):
        ruta = input("Introduce el nombre de la ruta original")
        ## comprobar que la ruta es correcta
        if not os.path.exists(ruta):
            print("ERROR\nLa ruta introducida no existe")
        else:
            ruta2 = input("Introduce el nombre de la ruta a la que copiar")
            ## comprobar que la ruta es correcta
            if not os.path.exists(ruta2):
                print("ERROR\nLa ruta introducida no existe")
            else:
                #shutil.copy(ruta,ruta2)
                        ##ruta_mod = ruta.split("/", -1)
                        ##ruta_mod = ruta_mod.pop(-1)
                ruta_mod = os.path.split(ruta)        ## El split con el path entiende que el separador es / y pilla el ultimo 
                ruta2 = os.path.join(ruta2,ruta_mod[1])
                shutil.copyfile(ruta,ruta2)
                print("Archivo copiado")

    def mover(self):
        ruta = input("Introduce el nombre de la ruta original")
        ## comprobar que la ruta es correcta
        if not os.path.exists(ruta):
            print("ERROR\nLa ruta introducida no existe")
        else:
            ruta2 = input("Introduce el nombre de la ruta a la que mover")
            ## comprobar que la ruta es correcta
            if not os.path.exists(ruta2):
                print("ERROR\nLa ruta introducida no existe")
            else:
                shutil.move(ruta,ruta2)
                print("Archivo movido")

    def eliminar(self):
        ruta = input("Introduce el nombre de la ruta")
        ## comprobar que la ruta es correcta
        if not os.path.exists(ruta):
            print("ERROR\nLa ruta introducida no existe")
        else:
            if os.path.isdir(ruta):
                ## es un directorio
                if(len(os.listdir(ruta)) == 0):
                    ## directorio vacio
                    os.rmdir(ruta)
                    print("Directorio eliminado")
                else:
                    print("El directorio no está vacío, no se puede eliminar")
            else:
                ## es un archivo
                os.remove(ruta)
                print("Archivo eliminado")

    def menu(self):
        print("SISTEMA DE ARCHIVOS\n¿Qué quieres hacer?\n\t[1] Crear un directorio\n\t[2] Listar un directorio\n\t[3] Copiar un archivo\n\t[4] Mover un archivo\n\t[5] Eliminar un archivo/directorio\n\t[6] Salir del programa")
        opcion = int(input())
        while(opcion<1 or opcion>6):
            print("Opcion Incorrecta")
            opcion = int(input())
        if(opcion==1):
            self.creardir()
        elif(opcion==2):
            self.listardir()
        elif(opcion==3):
            self.copiar()
        elif(opcion==4):
            self.mover()
        elif(opcion==5):
            self.eliminar()
        elif(opcion==6):
            exit(-1)
        self.menu()

var = ejercicio_menu()
var.menu()



