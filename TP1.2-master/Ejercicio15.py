#"Trabajo practico 1.2"
#Ejercicio 15

# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que 
# determine la hora de llegada a la ciudad B.

horas = int(input("Ingrese la hora de salida en (horas): "))
minutos = int(input("Ingrese la hora de salida en (minutos): "))
segundos = int(input("Ingrese la hora de salida en (segundos): "))

T = int(input("Ingrese el tiempo de viaje en segundos: "))

horas2 = T // 3600 #Cantidad de segundos ingresados por la cantidad de segundos equivalentes a 1 hora
s1 = T % 3600

minutos2 = s1 // 60 #cantidad de segundos restantes divididos en 60 segundos equivalentes a 1 minuto
s2 = s1 % 60  #Resto de los segundos que se muestran como menos de 60 segundos que equivalen a 1 minuto

horasF = horas + horas2
minutosF = minutos + minutos2
segundosF = segundos + s2

print(f"La hora de salida de la ciudad A es: {horas}:{minutos}:{segundos} hs")

print(f"La hora de llegada a la ciudad B es: {horasF}:{minutosF}:{segundosF} hs")

