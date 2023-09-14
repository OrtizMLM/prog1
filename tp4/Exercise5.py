# 5.Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.
for i in range(20):
    if i % 2 != 0:
        continue
    elif i == 0:
        continue
    print("Numero par: ",i)