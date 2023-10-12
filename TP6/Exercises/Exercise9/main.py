from matriz import *

row = 3
col = 3
let_low = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        let_low[i][j] = " "

for fila in let_low:
    print(fila)
tablero = mat(row, col)
print(tablero)
