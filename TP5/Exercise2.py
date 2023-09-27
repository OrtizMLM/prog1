# 2.Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.

def large ():
    st = str(input("Ingrese una frase: "))
    proces(st)

def proces (st):
    flag = 0 
    for i in st:
        flag += 1 
        if i == " ":       
            ult = flag
    if st[len(st)-1] == ' ':
        print("El ultimo caracter ingresado es un espacio! ")
    else:
        print(len(st[ult:]))


large()