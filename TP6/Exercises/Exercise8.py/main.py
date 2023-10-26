#Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, 
#participaron en un campeonato de fútbol con modalidad todos contra todos.
#Los goles anotados en cada encuentro se registraron en el siguiente cuadro:

#Escriba un programa que:
#      Lea el cuadro de goles en un arreglo de dos dimensiones.
#      Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#      Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#      Determine la cantidad de puntos obtenidos por cada equipo.
import random

goles_a_favor = []
goles_en_contra = []

contenedor = []

#CUADRO DE GOLES
for row in range(3):

    cuadro = []

    for column in range(3):

        goles = random.randint(0,10)

        cuadro.append(goles)
    
    contenedor.append(cuadro)



for elem in contenedor:
    print(elem)
    print("")

#CANTIDAD DE TRIUNFOS

triunfos = [[0]*3]*3
for row in range(len(contenedor)):
    for column in range(len(contenedor)):

        if contenedor[row][column] > contenedor[column][row]:

            triunfos[column][row] = 0
            triunfos[row][column] = 3

print("--------------")
for i in triunfos:
    print(i)
    print("")

#CANTIDAD DE DERROTAS

derrotas = [[0]*3]*3
for row in range(len(contenedor)):
    for column in range(len(contenedor)):

        if contenedor[row][column] < contenedor[column][row]:

            derrotas[column][row] = 3
            derrotas[row][column] = 0

print("--------------")
for i in derrotas:
    print(i)
    print("")


#CANTIDAD DE EMPATES

empates = [[0]*3]*3
for row in range(len(contenedor)):
    for column in range(len(contenedor)):

        if contenedor[row][column] == contenedor[column][row]:

            triunfos[column][row] = 1
            triunfos[row][column] = 1

print("--------------")
for i in empates:
    print(i)
    print("")


