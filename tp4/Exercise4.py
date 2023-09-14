#	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
# que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que 
# también sea divisible por 400.


startYear = int(input("Año inicial:"))
startFinish = int(input("Año final:"))
for year in range(startYear, startFinish+1):
   if not year %10 == 0:
       continue
   if not year %4 == 0:
       continue
   if year % 100 != 0 or year % 400 == 0:
       print(year)