# 3.Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, 
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. 
# Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254

def inp ():
    while True:
        nom = str(input("Ingrese su nombre y su apellido: "))
        if nom != "":
            dni = str(input("Ingrese su DNI: "))
            check(nom, dni)
        else:
            break

def check(st, dn):
    flag = 0
    while flag < 2:
        for i in st:
            if i == " ":
                flag +=1
            if flag >= 3:
                st = str(input("Puede ingresar solo dos nombre y un apellido: "))
                break
    while (len(dn) != 7) and (len(dn) != 8):
        dn = str(input("Ingrese porfavor correctamente el dni: "))
    fl = 0
    idd = ""
    for i in st:
        fl += 1
        if i == " ":
            idd = st[:(fl-1)]
            break
    nam = len(st[fl:])
    ident = idd+str(nam)+dn[:3]
    print(ident)

inp()