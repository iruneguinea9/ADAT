### Crea un programa en Python que pida al usuario 10 números y los guarde en una lista. Imprime la lista.

##          WHILE
#cont = 0
#lista = []
#while cont<10:
#    var = (int)(input("introduce un numero "))
#    lista.append(var)
#    cont = cont + 1
#print(lista)


##          FOR
lista = []
for numero in range(10):
    numero = (int)(input("introduce un numero "))
    lista.append(numero)
print(lista)