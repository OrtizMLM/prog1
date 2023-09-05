#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("Ingrese un numero: "))

impares =[]

for i in range(num):

    if i % 2 != 0:
        
        impares.append(i)

print(impares)

