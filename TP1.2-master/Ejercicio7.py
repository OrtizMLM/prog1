"Trabajo practico 1.2"
#Ejercicio 7

# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos

num = int(input("Ingrese la cantidad de minutos: "))

hora = int(num / 60)
min = num % 60

print(f"La cantidad de horas y minutos son: {hora} horas, {min} minutos")