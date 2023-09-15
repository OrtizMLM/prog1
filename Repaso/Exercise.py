# 1. Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el
# programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un
# signo de interrogación al final. El programa mostrará después la frase final.

text = str(input("Ingrese frase o palabra: "))

if len(text) == 4:
    print(text+"!")

else:
    print(text+"?")