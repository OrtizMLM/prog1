"Trabajo practico 1.2"
#Ejercicio 10
# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#	    55% del promedio de sus tres calificaciones parciales.
#	    30% de la calificación del examen final.
#	    15% de la calificación de un trabajo final.

parc1 = int(input("Ingrese nota parcial 1: "))
parc2 = int(input("Ingrese nota parcial 2: "))
parc3 = int(input("Ingrese nota parcial 3: "))

promParc = (parc1 + parc2 + parc3) / 3


parcF = (55 * promParc) / 100 # Formula para calcular % fijo del 55% del promedio de parciales

print(f"El promedio del 55% de los parciales es: {parcF}")

exfin = int(input("Ingrese nota del examen final: "))
calEx = (30 * exfin) / 100 # Formula para calcular % fijo del 30% de la calificacion del examen

print(f"El 30% del examen final es: {calEx}")

tpfin = int(input("Ingrese nota del Trabajo Practico final: "))
caltp = (15 * tpfin) / 100 # Formula para calcular % fijo del 15% de la calificacion del TP

print(f"El 15% del examen final es: {caltp}")

notfinal = (parcF + calEx + caltp) # La suma de las 3 notas con sus respectivos % da la nota final del alumno
print(f"La calificacion final del alumno es: {notfinal}")
