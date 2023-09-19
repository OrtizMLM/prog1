#Funciones

def add (dig):
    sum = 0
    for i in dig:    
        sum += int(i)
    print(f"Y la suma de sus digitos es: {sum}")
    return sum

#Main

num = str(input("Ingrese un numero: "))
acum = int(num)
while int(num) != 0:
    suma = add(num)
    num = str(input("Ingrese un numero: "))
    acum += int(num)
    print(f"La suma total de los numeros ingresados es: {acum}")
    if int(num) == 0:
        suma = add(str(acum))










