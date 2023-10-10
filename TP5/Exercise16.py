# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, 
# la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(number):
   f=1
   if number != 0:
       for i in range(1,number+1):
           f=f*i
   return f

 
amount = 0
num=int(input("Ingrese un numero (-1 termina): "))
while num != -1:
    print("Factorial:", factorial(num))
    amount += 1
    num = int(input("Ingrese un numero (-1 termina): "))
print(f"Se leyeron {amount} números")