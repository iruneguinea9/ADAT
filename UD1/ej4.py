### Adapta y amplia el programa anterior para que una vez introducidos los 10 números
#impares, se muestre un menú en pantalla con 5 opciones:

#¿Que desea hacer con la lista?
#1. Sumatorio
#2. Media
#3. Máximo
#4. Mínimo
#0. Salir


from statistics import mean

lista = []
for numero in range(10):
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
if opcion==1:
    #Sumatorio
    print("la suma de los elementos es: ", sum(lista))
elif opcion==2:
    #Media
    print("la media de los numeros de la lista es: ", mean(lista))
elif opcion ==3 :
    #Máximo
    print("El máximo de los elementos de la lista es ", max(lista))
elif opcion == 4:
    #Mínimo
    print("El mínimo de los elementos de la lista es ", min(lista))
