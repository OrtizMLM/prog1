
#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

amount = 0
num = int(input("Ingrese número: "))
while num != 0:
 primo = True
 for i in range(2,num):
   if num % i == 0:
     primo = False
     break
 if primo:
   amount += 1
 n = int(input("Ingrese número: "))
print(f"Cantidad de primos: {amount}")