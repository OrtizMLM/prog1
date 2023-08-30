"Trabajo practico 1.2"
#Ejercicio 11

# Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

print("Ingrese 2 numeros: ")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))

dist = abs (n1 - n2) #la distancia se calcula como la diferencia del 1ro con el 2do

print(f"La distancia entre los numeros ingresados es: {float(dist)}")