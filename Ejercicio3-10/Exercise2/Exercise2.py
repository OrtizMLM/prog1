#Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
#contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
#*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
#Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
#retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
#puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
#contenga cada domicilio una sola vez.

from funciones_2 import *


datos=[("ailen bossio",13,1500,"tacuari-579"),("juan busso",28,2000,"honorio-174")]

direcciones = facturas(datos)

print(direcciones)