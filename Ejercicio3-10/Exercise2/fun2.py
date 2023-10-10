#Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
#retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
#puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
#contenga cada domicilio una sola vez.

def facturas (datos):
    direcc = []

    for d in datos:

        direcc.append(d[3])

    return direcc
