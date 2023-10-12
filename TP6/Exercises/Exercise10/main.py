# 10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a.	la diagonal principal.
# b.	la diagonal inversa.
import random
row = int(input("Ingrese tamano de la matriz: "))
lst = ['A','A','B','B','C','C','D','D','CC']
matriz = [[random.choice(lst) for _ in range(row)] for _ in range(row)]
for rw in matriz:
    print(rw)
flag = 0
diag = []
for i in matriz:
    diag.append(matriz[flag][flag])
    flag += 1
invert = [matriz[i][len(matriz) - i - 1] for i in range(len(matriz))]
print(f"DIAGONAL PRINCIPAL: {diag}")
print(f"DIAGONAL INVERSA:{invert}")