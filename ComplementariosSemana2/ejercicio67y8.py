#Ejercico 6, 7 y 8: 

# Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio
#  Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le 
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 
#100% y el valor 0 al 0%.
#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y 
#almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que 
#aplicar la lógica de matemáticas.

precio = 1000
descuento = 0.25

precio_final = precio - (precio * descuento) 

print (precio_final)