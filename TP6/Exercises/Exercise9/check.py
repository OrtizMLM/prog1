from matriz import *
def prin (tab, row, col):
    for i in range(row):
        for j in range(col):
            if tab[i][j] == 0:
                print("X", end=" ")
            else:
                print(" ", end=" ")
            print("|", end=" ")
        print("\n" + "-" * (col * 4 - 1))