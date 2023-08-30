"Trabajo practico 1.2"
#Ejercicio 9
#	Una tienda ofrece un descuento del 15% sobre el total de la compra y 
# un cliente desea saber cuanto deberá pagar finalmente por su compra.

compra = float(input("Ingrese monto total de la compra: $"))

total = (15 * compra) / 100 # Formula para calcular % fijo del 15%

print(f"El descuento del 15% de la compra de ${compra} es de: ${round(total,2)}")