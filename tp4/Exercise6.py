# 6. Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
# Cuando encuentres el número, usa break para salir del bucle.
lis = [2,9,18,25,32]
num = int(input("ingrese un numero: "))
i = 0
for i in lis:
    print(i)
    if num != i:
        continue
    else:
        print("el nro igual es: ",i)
        break
