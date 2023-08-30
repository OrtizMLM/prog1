#Ejercicio 18

# Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante.
# A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina
#  Imprimir en pantalla el monto final a pagar.

valor_cena = float(input("Ingrese cuanto le costo su cena: "))
concepto_servicio = 0.062
propina = 0.10

total = valor_cena + valor_cena*concepto_servicio + valor_cena*propina

print(f"EL MONTO FINAL A PAGAR ES: {total}")