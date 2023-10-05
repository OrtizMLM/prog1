#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original
# y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], 
# la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]

def tup(lis):
    x = {}
    for i in lis:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    newli = [(i, x[i]) for i in x]
    return newli