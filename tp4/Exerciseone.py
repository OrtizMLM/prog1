#1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
# Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

line = str(input("Ingrese linea: "))
x = 0

while x < 6:
    x += 1
    print(line.upper())
    line = str(input("Ingrese linea: "))
    if x == 5:
        print("                            ")
        break

