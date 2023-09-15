# 2- Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra
# por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego

import random

list = ["futbol", "argentina", "fifa", "campeones", "francia"]
intent = 0
num = random.randint(0, len(list))
guess = list[num]
print(guess)
print(guess[len(guess)-1])
letter = str(input("Ingrese la primer letra: "))

while intent < 5:
    for i in guess:
        if letter == i:
            letter = str(input("Ingrese la proxima letra: "))
            if i == (guess[len(guess)-2]): 
                print("Adivinó")
                continue
        else:
            intent += 1
            print("Intentalo de nuevo. Intento:", intent)
            letter = str(input("Ingrese la primer letra: "))
            break
            