from matriz import *
from check import *

row = 3
col = 3
tab = mat(row, col)
for rw in tab:
    print(rw)
atte = 0
lett = 0
while lett <= 4:
    prin(tab, row, col)
    row1 = int(input("Ingrese la fila de la primera carta: ")) - 1
    col1 = int(input("Ingrese la columna de la primera carta: ")) - 1
    row2 = int(input("Ingrese la fila de la segunda carta: ")) - 1
    col2 = int(input("Ingrese la columna de la segunda carta: ")) - 1
    if (
                row1 < 0
                or row1 >= row
                or col1 < 0
                or col1 >= col
                or row2 < 0
                or row2 >= row
                or col2 < 0
                or col2 >= col
            ):
                print("Posición fuera de rango. Inténtalo de nuevo.")
                continue
    if tab[row1][col1] == tab[row2][col2]:
        lett += 1
        tab[row1][col1] = 0
        tab[row2][col2] = 0
        print("¡Encontraste una pareja!")
    else:
        print("Las cartas no coinciden. Intenta de nuevo.")
    atte += 1
print(f"Felicidades, ¡has encontrado todas las parejas en {atte} intentos!")