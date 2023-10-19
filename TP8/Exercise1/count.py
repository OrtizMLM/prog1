def count (num, cou):
    if cou == len(num):
        return print(f"Tiene {cou} digitos")
    if cou < len(num):
        cou +=1
        return count(num, cou)