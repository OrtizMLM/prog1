#10.La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 
#(210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. 
#A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). 
#Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo
#Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y 
#el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), 
#usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.
from med import *

med = int(input("Ingrese la medida(A): "))

print(f" La medida de A{med} es:{medidas_hoja_A(med)} milimetros")