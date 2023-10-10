#9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y 
#te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login,
# solamente tenemos tres oportunidades para intentarlo.

def login (n,p):
    if n == "usuario1" and p == "asdasd":

        print("VERDADERO")
        
        chance == 4

    else:
        chance += 1

    return chance
#main

chance = 0

while chance < 3 :

    name = str(input("Ingrese el nombre: "))

    passw = str (input("Ingrese la contraseña: "))

    login(name,passw)

if chance == 3:

    print("Ya se hicieron  3 intentos!")


