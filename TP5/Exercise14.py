# Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no
# sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar 
# la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del 
# mayor número ingresado.

def prime(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

 
def frequency(number,digit):
   amount=0
   while number!=0:
       lastDigit=number%10
       if lastDigit==digit:
           amount+=1
       number=number//10
   return amount

 
def factorial(number):
   f=1
   if number!=0:
       for i in range(1,number+1):
           f=f*i
   return f

 
def addDigit(number):
  add=0
  while number!=0:
      digit=number%10
      add=add+digit
      number=number//10
  return add

 
greater=0
number=int(input("Ingrese numero primo: "))
while prime(number):
    print(f"Suma de los dígitos: {addDigit(number)}")
    digit=int(input("Dígito: "))
    print(f"El {digit} aparece {frequency(number,digit)} veces")
    if number > greater:
          greater=number
    number=int(input("Ingrese numero primo: "))
print(f"Factorial de {greater} : {factorial(greater)}")