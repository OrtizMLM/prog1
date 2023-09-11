# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
# mostrar la sumatoria de todos los números ingresados

total = 0
num = int(input("Ingrese numeros a sumar: "))
while num != 0:
    total = total + num
    num = int(input("Ingrese otro numero o 0 para terminar: "))

print(f"La sumatoria total es: {total}")