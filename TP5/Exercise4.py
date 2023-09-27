# 4.Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def inp ():

    n1 = int(input("Ingrese un numero entero: "))
    n2 = int(input("Ingrese otro numero entero: "))
    check(n1, n2)

def check (num1, num2):
    if num1 % num2 == 0:
        print("El primero es multiplo del segundo")
    else:
        print("No son multiplo")

inp()