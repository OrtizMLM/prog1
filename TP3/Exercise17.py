#	Solicitar al usuario que ingrese una phrase y luego imprimir un listado de 
# las vocales que aparecen en esa phrase (sin repetirlas).

phrase = str(input("Escriba una frase: "))
amount = 0
for x in phrase:
    if x in "aeiou":
        amount = amount + 1
print(f"Cantidad de vocales:  {amount}")