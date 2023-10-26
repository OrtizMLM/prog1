def replicar_lista(lista, n):
    # Caso base: si la lista está vacía, no hay nada que replicar.
    if not lista:
        return []

    # Caso recursivo: replicar el primer elemento n veces y llamar a la función
    # recursivamente para el resto de la lista.
    elemento = lista[0]
    resto = replicar_lista(lista[1:], n)
    return [elemento] * n + resto

# Ejemplo de uso:
lista_original = [1, 3, 3, 7]
n = 2
lista_replicada = replicar_lista(lista_original, n)
print(lista_replicada)
