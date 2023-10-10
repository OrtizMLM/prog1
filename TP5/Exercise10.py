#11.	Escribir una función que reciba otra función y una lista, 
#y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def first (num):
    num += 5

    return num

def second (lista):

    lista2 = []

    for i in lista:

        lista2.append(first(i))

    return lista2

#main

lis = []

for i in range(5):

    n = int(input("ingrese un numero: "))
    lis.append(n)

print(second(lis))



