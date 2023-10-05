# 1.Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, 
# el cual no debe guardarse.
from Exercise2 import *
from Exercise3 import *
from Exercise4 import *
from Exercise5 import *

lis = []

num = int(input("Ingrese un numero: "))
while num != 0:
    lis.append(num)
    num = int(input("Ingrese un numero: "))
print(lis)
print(f"La lista con las tuplas: {tup(lis)}")
number = int(input("Ingrese un numero que desea eliminar: "))

lis = dele (lis, number) 
print(f"La lista nueva:{lis}")

print(f"La sumatoria de la lista es: {sum(lis)}")

men = int(input("Ingrese el numero menor: "))
print(f"La nueva lista con los menores que {men}: {newlist(lis, men)}")


