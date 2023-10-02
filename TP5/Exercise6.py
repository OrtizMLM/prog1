# 6.Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def space (text):
    text = " ".join([char if char != " " else " " for char in text])
    print(text)

def tex ():
    txt = str(input("Ingrese el texto: "))
    space(txt)

tex ()