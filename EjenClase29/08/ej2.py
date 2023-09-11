#  Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
#  0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#  Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total

total_pares = 0
total_impares = 0

num = int(input("Ingrese un numero entero positivo: "))

while num > 0:
   
    pares = 0
    impares = 0

    num = str(num)

    for i in num:
        dig = int(i)


        if dig % 2 == 0 :
            pares +=1

        else:
            impares += 1
    print(f"El numero {num} tiene {pares} numeros pares y {impares} numeros impares")

    total_pares += pares
    total_impares += impares

    num = int(input("Ingrese un numero entero positivo:"))

print(f"{total_pares} numeros pares leidos en total y {total_impares} numeros impares leidos en total")
print("Fin del programa")