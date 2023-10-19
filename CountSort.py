def countsort(A, k):
 
    # crea una lista de enteros de tamaño `n` para almacenar la lista ordenada
    output = [0] * len(A)
 
    # crea una lista de enteros de tamaño `k + 1`, inicializada por todos cero
    freq = [0] * (k + 1)
 
    # usando el valor de cada elemento en la lista de entrada como un índice,
    # almacena el conteo de cada entero en `freq[]`
    for i in A:
        freq[i] = freq[i] + 1
 
    # calcula el índice inicial para cada entero
    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount
 
    # copia a la lista de salida, conservando el orden de las entradas con teclas iguales
    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1
 
    # copia la lista de salida de nuevo a la lista de entrada
    for i in range(len(A)):
        A[i] = output[i]
    return A