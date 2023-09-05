# 12-Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

key = str(input("Ingrese una letra: "))
sen = str(input("Ingrese una frase: "))
flag = 0

for i in sen:
    if key == i:
        flag += 1
print("La letra aparece:",flag,"veces")
