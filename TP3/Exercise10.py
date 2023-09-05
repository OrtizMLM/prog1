# 10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = int(input("Ingrese numero: "))
x = 1
c = 0 

while x <= num:
    if num % x == 0:
        c = c + 1
    x = x + 1

if c == 2: 
    print("El numero ",num," Es primo")
else:
    print("El numero ",num," No es primo")
