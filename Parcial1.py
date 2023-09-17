# Realizar un programa que cumpla con las siguientes condiciones:

# Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
# Generar un menú de opciones, que serán:
# Juego de números.
# Juego de palabras.
# Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
# El mayor número par.
# El promedio de los números impares.
# Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
# No olvides realizar las debidas validaciones!

# INICIO DEL PROGRAMA

name = str(input("Ingrese su nombre: "))

menu = int(input(f"Hola {name} elegí un juego: 1) Juego de números. 2) Juego de palabras. "))

# JUEGO DE NÚMEROS
if menu == 1:
    numer = 1
    par = []
    impar = []
    while numer != 0:
        numer = int(input(f"{name} ingresá numeros enteros, cuando finalices ingresa un 0: "))
        if numer % 2 == 0:
            par.append(numer)
        else:
            impar.append(numer)
    print(f"{name} El mayor de los pares es: {max(par)}") # MOSTRAMOS POR PANTALLA EL PAR MAYOR
    average = 0
    flag = 0
    for i in impar:
        flag += 1
        average += i
    print(f"{name} El promedio de los impares es: {average/flag}") # MOSTRAMOS POR PANTALLA EL PROMEDIO DE IMPARES

#JUEGO DE PALABRAS
elif menu == 2:
    text = str(input(f"{name} ingresa una frase: "))
    text = text.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for x in text:
        if x == "a":
            a += 1
        elif x == "e":
            e += 1
        elif x == "o":
            o += 1
        elif x == "i":
            i += 1
        elif x == "u":
            u += 1
    print(f"{name} La cantidad de veces que aparece A -> {a}")
    print(f"{name} La cantidad de veces que aparece E -> {e}")
    print(f"{name} La cantidad de veces que aparece I -> {i}")
    print(f"{name} La cantidad de veces que aparece O -> {o}")
    print(f"{name} La cantidad de veces que aparece U -> {u}")
else:
    print(f"{name} Ingresa '1' o '2', vuelve a intentarlo.")

# FIN DEL PROGRAMA.