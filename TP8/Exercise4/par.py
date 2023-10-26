from impar import *

def par(n):
    if n % 2 == 0:
        return print("El numero es par")
    else:
        return impar(n)