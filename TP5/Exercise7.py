# 7.Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, 
# utilizando la función anterior.

def numbers ():
    num_list = []

    for i in range(10):

        num = int (input("ingrese 10 numeros enteros: "))

        num_list.append(num)

    greater_than(num_list)
    less_than(num_list)

def greater_than (nl):

    print(f"EL mayor es: {max(nl)}")

def less_than (nl):

    print(f"El menor es: {min(nl)}")

numbers ()