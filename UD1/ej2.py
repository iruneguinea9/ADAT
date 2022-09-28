### Modifica el programa anterior, de manera que al terminar de guardar los números en la lista se impriman la lista,
# #el sumatorio y la media de todos los número de dicha lista.
from statistics import mean

lista = []
for numero in range(10):
    numero = (int)(input("introduce un numero "))
    lista.append(numero)
print("lista: " , lista)
print("la suma de los elementos es: ",sum(lista))
print("la media de los numeros de la lista es: ",mean(lista))

