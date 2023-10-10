# 	Solicitar al usuario un número entero y luego un dígito. Informar la amount de ocurrencias del
# dígito en el número, utilizando para ello una función que calcule la frecuencia

def frequency(number,digit):
   amount = 0
   while number != 0:
       lastDigit = number%10
       if lastDigit == digit:
           amount += 1
       number = number//10
   return amount

 
num = int(input("Ingrese numero: "))
one_digit=int(input("Ingrese digito: "))
print(f"Frecuencia del dígito en el número:{frequency(num,one_digit)}")