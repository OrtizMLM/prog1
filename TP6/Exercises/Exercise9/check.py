from main import *
from matriz import *
def imprimir_tablero(tablero, row, col):
    for i in range(row):
        for j in range(col):
            if tablero[i][j] == 0:
                print("X", end=" ")
            else:
                print(" ", end=" ")
            print("|", end=" ")
        print("\n" + "-" * (col * 4 - 1))