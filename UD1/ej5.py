### Modifica el programa anterior de forma que cada una de las funcionalidades del programa se
# ejecute mediante una función.

## FUNCIONES

def sumatorio (lista):
    """Esta funcion sirve para hacer la función de sumatorio"""
    suma = 0
    lista = list(lista)
    for numero in range(len(lista)):
        suma = suma + lista[numero]
    return suma
def media (lista):
    """Esta funcion sirve para hacer la media"""
    media = 0
    lista = list(lista)
    media = sumatorio(lista)/len(lista)
    return media

def maximo(lista):
    """Esta funcion sirve para calcular el maximo de una lista"""
    lista = list(lista)
    max = -1
    for i in range (len(lista)):
        if(lista[i]>max):
            max = lista[i]
    return max

def minimo(lista):
    """Esta funcion sirve para calcular el minimo de una lista"""
    lista = list(lista)
    min = lista[0]

    for i in range (len(lista)-1):
        if(lista[i+1]<min):
            min = lista[i+1]
    return min

lista = []
for numero in range(3):
    numero = (int)(input("introduce un numero impar"))
    while(numero%2==0):
        print("Error, introduce un numero impar")
        numero = (int)(input("Vuelve a introducir el numero"))
    lista.append(numero)
print("Lista: ",lista)
print("¿Que desea hacer con la lista?")
print("1. Sumatorio\n2. Media\n3. Máximo\n4. Mínimo\n0. Salir")
opcion = (int)(input())
while(opcion<0 or opcion>4):
    print("Error, opcion no valida")
    opcion = (int)(input())
if opcion == 1:
    #Sumatorio
    print("la suma de los elementos es: ", sumatorio(lista))
elif opcion == 2:
    #Media
    print("la media de los numeros de la lista es: ",media(lista))
elif opcion == 3:
    #Máximo
    print("El máximo de los elementos de la lista es ", maximo(lista))
elif opcion == 4:
    #Mínimo
    print("El mínimo de los elementos de la lista es ", minimo(lista))
