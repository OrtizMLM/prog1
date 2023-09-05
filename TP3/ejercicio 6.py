#Escribir un programa que pida al usuario un número entero 
#y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.


num = int(input("ingrese un numero entero positivo: "))

tri = []

for i in range(num):
    tri.append("*")

    print(tri)

   