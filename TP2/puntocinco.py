letra = str(input("Ingrese una letra: "))
if len(letra) == 2:
    print("No se puede procesar el dato")
elif letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or  letra.lower() == "u":
        print("Es vocal")
else:
    print("no vocal")