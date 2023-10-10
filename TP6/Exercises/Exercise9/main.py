from matriz import *

row = 3
col = 3
let_low = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        let_low[i][j] = " "

for fila in let_low:
    print(fila)
tablero = mat(row, col)
print(tablero)


# if (
#             fila1 < 0
#             or fila1 >= filas
#             or columna1 < 0
#             or columna1 >= columnas
#             or fila2 < 0
#             or fila2 >= filas
#             or columna2 < 0
#             or columna2 >= columnas
#         ):
#             print("Posición fuera de rango. Inténtalo de nuevo.")
#             continue
    


# import random
# def jugar_memoria():
#     filas = int(input("Ingrese el número de filas del tablero: "))
#     columnas = int(input("Ingrese el número de columnas del tablero: "))

#     if filas * columnas % 2 != 0:
#         print("El número de cartas debe ser par.")
#         return

#     tablero = inicializar_tablero(filas, columnas)
#     cartas_encontradas = []
#     intentos = 0

#     while len(cartas_encontradas) < filas * columnas:
#         imprimir_tablero(tablero, filas, columnas)
#         print("Cartas encontradas:", cartas_encontradas)
#         fila1 = int(input("Ingrese la fila de la primera carta: ")) - 1
#         columna1 = int(input("Ingrese la columna de la primera carta: ")) - 1
#         fila2 = int(input("Ingrese la fila de la segunda carta: ")) - 1
#         columna2 = int(input("Ingrese la columna de la segunda carta: ")) - 1

#         if (
#             fila1 < 0
#             or fila1 >= filas
#             or columna1 < 0
#             or columna1 >= columnas
#             or fila2 < 0
#             or fila2 >= filas
#             or columna2 < 0
#             or columna2 >= columnas
#         ):
#             print("Posición fuera de rango. Inténtalo de nuevo.")
#             continue

#         if tablero[fila1][columna1] == tablero[fila2][columna2]:
#             cartas_encontradas.append(tablero[fila1][columna1])
#             tablero[fila1][columna1] = 0
#             tablero[fila2][columna2] = 0
#             print("¡Encontraste una pareja!")
#         else:
#             print("Las cartas no coinciden. Intenta de nuevo.")
        
#         intentos += 1

#     print(f"Felicidades, ¡has encontrado todas las parejas en {intentos} intentos!")

# if __name__ == "__main__":
#     jugar_memoria()

# def imprimir_tablero(tablero, filas, columnas):
#     for i in range(filas):
#         for j in range(columnas):
#             if tablero[i][j] == 0:
#                 print("X", end=" ")
#             else:
#                 print(" ", end=" ")
#             print("|", end=" ")
#         print("\n" + "-" * (columnas * 4 - 1))

# # Función principal del juego

# # Función para inicializar el tablero con cartas aleatorias
# def inicializar_tablero(filas, columnas):
#     numeros = list(range(1, (filas * columnas) // 2 + 1))
#     cartas = numeros + numeros
#     random.shuffle(cartas)
#     tablero = [[0] * columnas for _ in range(filas)]
#     for i in range(filas):
#         for j in range(columnas):
#             tablero[i][j] = cartas.pop()
#     for fila in tablero:
#         print(fila)
#     return tablero

# Función para imprimir el tablero con las cartas boca abajo