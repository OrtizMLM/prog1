# Ejercicio 20

# Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

fecha = str(input("Ingrese el dia de su nacimiento: "))
dia = fecha[0:2]
mes = fecha[2:4]
anio = fecha[4:8]




print(f"La variable con el formato DDMMAAA es: ",dia,mes,anio)