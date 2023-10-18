import random

flag = 0

def time(flag):
    option = random.randint(1,3)
    if option == 3:
        flag += 7 
        return print((f"La rata salio, total del tiempo: {flag}"))
    if option == 1:
        flag += 3
        print(f"Se demoro en volver 3 min, total de tiempo: {flag}")
        return (flag)
    if option == 2:
        flag += 5
        print(f"Se tardo en volver 5 minutos, total del tiempo: {flag}")
        return time(flag)

time(flag)