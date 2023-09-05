# 15-Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num = int(input("Ingrese un numero mayor que 0: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i,"es un divisor de",num)