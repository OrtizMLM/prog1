# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
# Informar cuál fue el bignum número ingresado.

bignum = -1
num = int(input("Ingrese numero positivo: "))
while num >= 0:
    if num > bignum:
       bignum = num
    num = int(input("Número positivo:"))
    if num == 0 :
        print(f"El mayo numero es: {bignum}")
        break
print("fin programa")
