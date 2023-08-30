# Ejercicio 20

# Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

dia = int(input("Ingrese el dia de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
año = int(input("Ingrese el año de su nacimiento: "))
var = str(dia) +"/"+ str(mes) + "/" + str(año)

print(f"La variable con el formato DDMMAAA es: " + var)