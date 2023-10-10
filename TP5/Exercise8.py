# Escribir una función que calcule el módulo de un vector.

def sum_square(x, y):

    return x + y ** 2

def module(v):
    
    
    from functools import reduce
    return reduce(sum_square, v, 0) ** 0.5

print(module((2, 6)))
print(module((2, 3, 4)))