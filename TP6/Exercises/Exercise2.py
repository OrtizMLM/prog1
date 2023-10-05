#2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. 
# Mostrar un mensaje si no es posible eliminar.
def dele (li, num):
    if num in li:
        li.remove(num)
    return li    