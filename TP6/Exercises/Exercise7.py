#Escribir un programa que procese strings ingresados por el usuario.
# La lectura finaliza cuando se hayan procesado 50 strings. 
#Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados.
# Ejemplo:
#‘r’:5
#‘%’:3
#‘a’:8
#‘9’:1

list_words = {}

for i in range(5):

    word = str(input("ingrese un string: "))
    
    for c in word:

        if c not in list_words:

            list_words[c] = 1

        else:

            list_words[c] += 1

for word,c in list_words.items():

    print(f"{word} : {c}")
    


   
