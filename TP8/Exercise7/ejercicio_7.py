#7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
#K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
#   ● El programa debe pedir al usuario que ingrese un número n, y un número d,
#   ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
#   ● Debe imprimir el resultado de K(n, p)

def k(n,p):

    if n == 1:

        return p*1
    
    else:

        return p*n + k(n-1,p)

#MAIN

n = int(input("ingrese un numero: "))
p = int(input("ingrese otro numero: "))

print(k(n,p))