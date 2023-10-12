# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario
# debe mostrar un mensaje informando de ello.

dic = {'Banana': 50, 'Manzana': 40, 'Pera': 80, 'Frutilla': 120, 'Naranja': 80}

fruit = str(input("Ingrese una fruta: "))

if fruit in dic:
    kg = float(input("Ingrese los kg que quiere: "))
    print(f"El precio de {kg} KG de {fruit} es ${dic[fruit]*kg}")
else:
    print("La fruta no esta en el diccionario.")