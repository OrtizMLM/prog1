# 14-Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))

for i in range(num1, num2):
    if i % 2 == 0:
        print(i,"es par.")
    else:
        print(i,"es impar")