
# Cuenta bancaria

balance = 0
print ("Escriba la bitacora de operaciones: ")
while True:
    amounts = input()
    if not amounts:
        break
    info = amounts.split(" ")
    operacion = info[0]
    monto = int(info[1])
    if operacion=="D":
        balance+=monto
    elif operacion=="R":
        balance-=monto
    else:
        pass
print (balance)




