#2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.


def potencia(p,n):

  if n == 0:

    return False
  
  if n == 1:

    return True
  
  a = 1

  while a <= n:

    if a == n:
      
      return True
     
    a *= p


#main

p = int(input("Ingrese un numero entero: "))
n=int(input("ingrese otro numero entero: "))

if potencia(p,n) == True:
  
  print(f"{n} es potencia de {p}")

else:
  
  print(f"{n} NO es potencia de {p}")

