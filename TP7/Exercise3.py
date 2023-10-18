# 3.Crea una lista de diccionarios, donde cada diccionario contiene información sobre un book 
# (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de books en función de un campo específico,
# como el año de publicación o el autor.

lst = [
    {'titulo': 'Don Quijote', 'ano': 1950, 'autor': 'Miguel de Cervantes'},
    {'titulo': 'Martin Fierro', 'ano': 1920, 'autor': 'José Hernández'},
    {'titulo': 'Lupin', 'ano': 1980, 'autor': 'Maurice Leblanc'}
]

for i in range(len(lst) - 1):
    menor = i  # índice del primer elemento por default será el mínimo

    for j in range(i + 1, len(lst)):
        if lst[j]['ano'] < lst[menor]['ano']:
            menor = j

    if menor != i:
        # Intercambiar los diccionarios, no solo los años
        lst[menor], lst[i] = lst[i], lst[menor]

# Imprimir la lista de books ordenada por año de publicación
for book in lst:
    print(f'Título: {book["titulo"]}, Autor: {book["autor"]}, Año de Publicación: {book["ano"]}')