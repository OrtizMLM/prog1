# 11.Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

div = str(input("Ingrese el nombre de la divisa: "))
dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

if div in dic:
    sim = dic[div]
    print(f"El simbolo de {div} es: {sim}")
else:
    print(f" {div} la divisa no está en el diccionario.")