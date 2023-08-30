"Trabajo practico 1.2"
#Ejercicio 14

# 	Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen 
# al final las dos variables.

A = int(input("Ingrese variable numerica A : "))
B = int(input("Ingrese la variable numerica B : "))

A , B = B , A # aca declaramos que A toma el lugar de B y B el lugar de A

print(f"Los valores fueron cambiados, el nuevo valor de A es: {A} y el nuevo valor de B es: {B} ")


