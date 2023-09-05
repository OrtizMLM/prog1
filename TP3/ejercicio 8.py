#Escribir un programa que pida al usuario un número entero y
# muestre por pantalla un triángulo rectángulo como el de más abajo.

num = int(input("Ingrese un numero entero positvo: "))

arrays =[]

for i in range(num+1):

    if (i) % 2 != 0:

        arrays.append(i)

        arrays_invert = arrays[::-1]

        print(arrays_invert) 

         
