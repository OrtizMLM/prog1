# 16-Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

num = int(input("Ingrese la cantidad de numeros que desea: "))
i = 0
quest = float(input("Ingrese el numero: "))
while i < num: 
    if quest < 0:
        print(quest,"Es negativo")
        i += 1
    else:
        print(quest,"Es positivo")
        i += 1
    quest = float(input("Ingrese otro numero: "))
    