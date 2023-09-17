# 3. Escribe un programa que cuente cuántas palabras hay en una cadena de texto ingresada por el usuario

text = str(input("Ingrese frase: "))
flag = 1

for i in text:
    if i == " ":
        flag += 1
print(flag)