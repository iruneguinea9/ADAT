### Modifica el programa anterior de forma que la lista de 10 números sean números impares.
#(hay que asegurarse de que lo que se introduce en la lista son números).
from statistics import mean

lista = []
for numero in range(10):
    numero = (int)(input("introduce un numero impar"))
    while(numero%2==0):
        print("Error, introduce un numero impar")
        numero = (int)(input("Vuelve a introducir el numero"))
    lista.append(numero)
print("lista: " , lista)
print("la suma de los elementos es: ",sum(lista))
print("la media de los numeros de la lista es: ",mean(lista))