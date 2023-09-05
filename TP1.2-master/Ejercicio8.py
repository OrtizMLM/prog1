"Trabajo practico 1.2"
#Ejercicio 8

#	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas 
# que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.


sueldo = float(input("Ingrese sueldo base: $"))

comision = (10 * sueldo) / 100 # Formula para calcular % fijo del 10%

print(f"La comision del 10% de ${sueldo} por las tres ventas es: $",comision*3)
