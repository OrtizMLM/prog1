nro1 = float(input("Ingrese el primer numero: "))
nro2 = float(input("Ingrese el segundo numero: "))
nro3 = float(input("Ingrese el tercer numero: "))

if (nro1 < nro2) and (nro1 < nro3):
    print("El menor es el primer numero")
elif (nro2 < nro1) and (nro2 < nro3):
    print("El menor es el segundo")
elif (nro1 < nro3) and (nro1 == nro2):
    print("Los menores son el primero y el segundo")
elif (nro1 < nro2) and (nro1 == nro3):
    print("Los menores son el primero y el tercero")
elif (nro2 < nro1) and (nro2 == nro3):
    print("Los menores son el segundo y el tercero")
elif (nro1 == nro2 and nro1 == nro3):
    print("Los tres valores ingresados son iguales")
else:
    print("El menor es el tercero")