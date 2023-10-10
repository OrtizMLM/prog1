# 	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una
# función booleana que lo decida.

def prime(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
number = int(input("Ingrese numero: "))
if prime(number):
    print("Es primo")
else:
    print("No es primo")