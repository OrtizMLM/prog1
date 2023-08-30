#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
#Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un numero entero: "))

if num1 <= 0 or num2 <= 0 :
    print("ERROR, valor nulo o negativo")

else:
    if num1 > num2 :
        
        if num1 % num2 == 0 :
           print(f"El numero {num1} es multiplo de {num2}")

        else:
            print(f"El numero {num1} no es multiplo de {num2}")

    elif num2 > num1  :
        
        if num2 % num1 == 0 :
            print(f"El numero {num2} es multiplo de {num1}")

        else:
            print(f"El numero {num2} no es multiplo de {num1}")

    else:
        print("Los numeros son iguales!")
         

