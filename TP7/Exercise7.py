#7.	Crea una lista que contenga tanto números como st de caracteres. Escribe un programa que ordene esta lista de manera 
#que primero estén los números ordenados de menor a mayor y luego las st de caracteres ordenadas alfabéticamente.
# Lista con números y st de caracteres
lst = [10, "manzana", 5, "pera", "uva", "fresa", 8, 3, 1, 19, 14, 2, 12, 12.5, "kiwi", "banana", "25", 3]

num = [x for x in lst if isinstance(x, int)]
st = [x for x in lst if isinstance(x, str)]


num.sort()
st.sort()

lst_ord = num + st

print(lst_ord)
