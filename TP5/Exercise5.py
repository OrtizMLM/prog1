# 5. Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# # Crear un programa principal, que utilizando la función anterior, 
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número 
# de días que se van a introducir.


def calc (max, min):
    med = (max+min)/2
    print(f"La media es: {int(med)}")

def dat ():
    day = int(input("Ingrese la cantidad de dias que quiere introducir: "))
    for i in range(day):
        max = int(input(f"Ingrese la maxima del dia {i+1}: "))
        min = int(input(f"Ingrese la minima del dia {i+1}: "))
        calc(max, min)
        
dat()