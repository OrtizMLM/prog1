#Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, 
#y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

invest = float(input("Ingrese la cantidad a invertir: "))

interest = float(input("Ingrese el interes anual: "))

years = int(input("Ingrese la cantidad de años: "))


for i in range(years):

    invest += (invest*interest)/100

print(f"El capital obtenido es de : ${invest}") 