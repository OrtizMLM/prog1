#8.	Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
import math
pi = math.pi

def circ ():

    radio = float(input("Ingrese el radio de la circunferencia: "))

    calc_area(radio)
    calc_perim(radio)

def calc_area (rad):

        area = 2 * pi * rad

        print(f"El area es: {area}")

def calc_perim (rad):
      
      perim = pi * rad ** 2

      print(f"El perimetro es: {perim}")

circ()
