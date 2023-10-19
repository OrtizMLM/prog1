#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.


lis = [8, 3, 1, 19, 14, 2, 12, 12.5]

n = len(lis)
  
for i in range(n-1):
    for j in range(n-1-i):
        if lis[j] < lis[j+1]:
            lis[j], lis[j+1] = lis[j+1], lis[j]

print(lis)