#10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios
# y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.

def descuentos (dicc):
    total = 0
   
    for p,d in dicc.items():

        total += p - (p * d / 100)

    return total

#main
dicc = {} 
for i in range (5):

    precio = int(input("ingrese precio: "))
    descuento = int(input("ingrese descuento: "))

    dicc[precio] = descuento

resultado = descuentos(dicc)

print (resultado)

