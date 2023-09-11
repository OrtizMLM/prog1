# 	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene
# multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 
# El factorial de 0 es 1.

num = int(input("Ingrese el num a saber factorial:"))
fact = 1
if num != 0:
    for i in range(1,num+1):
        fact = fact * i
print(f"El factorial del num ingresado es: {fact}")