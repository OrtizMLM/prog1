#8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera:
# Las filas se enumeran desde n = 0, de arriba hacia abajo.
# Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). 
#Los valores que se encuentran en los bordes del triángulo son todos unos.
# Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. 
#Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

def pascal(filas) :
    fila = [1]
    cero = [0]
    
    for i in range(filas):
        print(fila)
        
        fila = [i + d for i, d in zip(fila + cero, cero + fila)]
        
pascal(5)

