"Trabajo practico 1.2"
#Ejercicio 12

# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

num = int(input("Ingrese numero a saber raiz cuadrada y cubica: "))

pot2 = num **(1/2) # calculo de la raiz cuadrada sin metodos solo comando puro
pot3 = num **(1/3) # calculo de la raiz cubica igual sin metodos solo comandos propios

print(f"La raiz cuadrada del numero ingresado es: {pot2} y la raiz cubica es: {pot3}")