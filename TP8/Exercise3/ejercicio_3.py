#3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y 
#devuelva una lista con las posiciones en donde se encuentra b dentro de a.


def positions(a,b,count,pos):

    if count == len(a):

        return pos
    
    if count < len (a):

        if b == a[count]:
            
            pos.append(count)
        
        return positions(a,b,count+1,pos)



#MAIN
a = input("ingrese un string: ")
b = input("ingrese otro string: ")

count = 0
pos = []

print(positions(a,b,count,pos))
