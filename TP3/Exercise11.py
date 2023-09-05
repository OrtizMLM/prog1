# Ejercicio 11
# 11-Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
# introducida empezando por la última.

key = str(input("Ingrese una palabra: "))
flag = len(key)


for i in key:
    print(key[flag-1])
    flag -= 1
    