#4- Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.
lst = ["manzana", "pera", "uva", "fresa", "kiwi"]
def insert(lis):
    for i in range(len(lis)):
        key = lis[i]
        j = i - 1
        while j >= 0 and len(key) < len(lis[j]):
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key
    print(lst)

insert(lst) 