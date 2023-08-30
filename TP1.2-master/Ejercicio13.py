"Trabajo practico 1.2"
#Ejercicio 13

#	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32

num = int(input("Ingrese un numero de 2 digitos: "))

c2 = num % 10 # el modulo de 10 es corriendo la coma del digito 2 para dar el valor deseado
c1 = int((num % 100) / 10) # declaramos entero para que nos de el digito 1 sin comas

print(f"El numero invertido es: {str(c2)}{str(c1)}")