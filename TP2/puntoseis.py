ano = int(input("Ingrese ano: "))
if (ano % 100 != 0 and ano % 4 == 0 ) or (ano % 400 == 0 ):
    print("Es biciesto")
else:
    print("No es biciesto")