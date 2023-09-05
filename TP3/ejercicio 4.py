#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Ingrese un numero entero positivo: "))

count = []

for i in range(num):

    count.append(i)

count_invert = count[::-1]

print(count_invert)
