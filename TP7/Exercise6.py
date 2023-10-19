# 6.Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.
import sys
sys.path.append("G:\Mi unidad\Prog 1\prog1")
import CountSort

A = [4, 2, 10, 10, 1, 4, 2, 1, 10, 8]
k = 11

print(CountSort.countsort(A, k))
