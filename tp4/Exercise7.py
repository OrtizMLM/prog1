#7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
#Utiliza un bucle while para permitir al usuario seleccionar una opción. 
#Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

option = int(input("Ingrese una opcion: (1), (2) o (3): "))

while option != "":
    print("La opcion elegida es: ",option)
    if option == 0:
        break
    option = int(input("Ingrese una opcion: (1), (2) o (3) "))