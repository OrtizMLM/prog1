# 9- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
# usuario por la contraseña hasta que introduzca la contraseña correcta.

password = "Programa"
pas = str(input("Ingrese contrasena: "))

while pas != password:
    print("Contrasena incorrecta, vuelva a a intentarlo ")
    pas = str(input("Ingrese contrasena: "))
print("contrasena correcta")