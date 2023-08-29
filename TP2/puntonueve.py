#Ejercicio 9
#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior 
#a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre 
#por pantalla el grupo que le corresponde.

sexo = str(input("Ingrese sexo (hombre/mujer): "))
nombre = str(input("Ingrese nombre: "))
nombre = nombre.lower()
if sexo.lower() == "hombre" and nombre[0] > "n" or (sexo.lower() == "mujer" and nombre[0] < "m"):
    print("pertenece al grupo A")
else:
    print("Pertenece al grupo B")
