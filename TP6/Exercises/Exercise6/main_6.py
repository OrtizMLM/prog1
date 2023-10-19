#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
#finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos
# de nivel secundario, finalizando al ingresar ‘x’.
#   Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
#   Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#   Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

from funciones_6 import *

print("INGRESE LOS NOMBRES DE LOS ALUMNOS DE NIVEL PRIMARIO")
print("Escriba 'X' cuando termine de ingresar los nombres")

name = 'o'

names_p = []
names_s = []

while name != 'x':

    name = str(input("Nombre: "))

    if name != 'o':

        names_p.append(name)


print("INGRESE LOS NOMBRES DE LOS ALUMNOS DE NIVEL PRIMARIO")
print("Escriba 'X' cuando termine de ingresar los nombres")

name = 'o'

while name != 'x':

    name = str(input("Nombre: "))

    if name != 'o':

        names_s.append(name)

sh = show(names_p,names_s)

r = repeat(names_p,names_s)

nr = no_repeat(names_p,names_s)

print(sh)
print(r)
print(nr)