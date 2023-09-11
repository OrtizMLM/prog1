# Crear un programa que permita al usuario ingresar los amounts de las compras de un cliente
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el amount 0.

total = 0
amount = float(input("Monto de una venta: $ "))
while amount!=0:
    if amount<0:
        print("monto no válido.")
    else:
        total+=amount
    amount=float(input("monto de una venta: $ "))
if total>1000:
    total = total - (total*0.1)
print(f"Monto total a pagar: $ {total}")