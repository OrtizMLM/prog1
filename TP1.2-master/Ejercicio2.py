"Trabajo practico 1.2"
#Ejercicio 2

lado1 = 0
lado2 = int(input("Ingrese valor del lado 2: "))
lado3 = int(input("Ingrese valor del lado 3: "))

hipotenusa = lado1 # Aclaramos que el lado 1 va a ser la hipotenusa a calcular

lado1 = ((lado2)**2 + (lado3)**2)**0.5 # Aplicamos la formula tradicional del calculo de hipotenusa a^2=b^2+c^2

print(f"La hipotenusa del triangulo es: {lado1}")