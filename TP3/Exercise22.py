
#	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los 
# dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar 
# cuántos de los números ingresados por el usuario fueron números pares.

peers = 0
n = int(input("Número (-1 para terminar el programa): "))
while n!=-1:
    if n%2 == 0:
        peers+=1
    add = 0
    while n!=0:
        digit = n % 10
        add+=digit
        n = n//10
    print(f"suma de sus dígitos: {add}")
    n = int(input("Número (-1 para terminar el programa): "))
print(f"Se ingresaron {peers} números pares")