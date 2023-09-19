#Funciones

def add (dig):
    sum = 0
    for i in dig:    
        sum += int(i)
    print(sum)
    return sum

#Main

num = str(input("Ingrese un numero: "))
while int(num) != 0:
    suma = add(num)
    num = str(input("Ingrese un numero: "))
    
    










