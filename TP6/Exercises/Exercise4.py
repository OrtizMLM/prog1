#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. 
#Imprimir esta nueva lista, iterando por ella.
def newlist(lis, men):
    new = []    
    for i in lis:
        if i < men:
            new.append(i)
    return new

