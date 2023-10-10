import random
def mat(row, col):
    letter = ['A','A','B','B','C','C','D','D','COMODIN']
    matriz = [[0 for _ in range(col)] for _ in range(row)]
    val_only = random.sample(letter, row * col)
    for i in range(row):
        for j in range(col):
            matriz[i][j] = val_only.pop()
    return matriz

    # Llenar la matriz con los valores aleatorios de la li
