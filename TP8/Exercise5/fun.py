def fun(lst, x, big):
    if x == (len(lst)):
        return (f"El mayor es {big}")
    if big < lst[x]:
        big = lst[x]
        x += 1
        return fun(lst, x, big)
    else:
        x += 1
        return fun(lst, x, big)

    