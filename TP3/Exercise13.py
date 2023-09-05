# 13-Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

eco = str(input("Ingrese algo: "))

while eco != "salir":
    print(eco)
    eco = str(input("Ingrese algo: "))