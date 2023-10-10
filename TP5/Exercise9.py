#	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que 
# contiene y su longitud

def length_words(sentence):
    
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

sentence = input("Ingrese una frase: ")
print(length_words(sentence))