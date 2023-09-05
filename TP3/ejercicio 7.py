#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range (10):

    for j in range (10):

        rest = (i+1) * (j+1)

        print(f"{i+1} x {j+1} = {rest}")
