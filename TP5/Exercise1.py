# 1.Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def inp ():
    dni = str(input("Ingrese numero de DNI: "))
    verif(dni)
    return dni


def verif (dni):
    if len(dni) == 7 or len(dni) == 8:
        print("True")
        return True
    else:
        print("False")
        return False
        
inp()

    

