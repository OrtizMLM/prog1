# 	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
# que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra 
# vez las cantidades que se irán ahorrando, hasta que el total saved iguale o supere al accumulate. 
# El programa deberá comprobar que las cantidades ingresadas sean positivas

print("Alcancia!")

accumulate = float(input("Ingrese el monto deseado a acumular: $ "))

while accumulate < 0:
        print("Por favor, escriba una cantidad positiva.")
        accumulate = float(input("¿Cuántos pesos quiere ahorrar?: $ "))

saved = 0.0
while accumulate > saved:
    saving = float(input("¿Cuántos pesos quiere meter en la alcancia?: $  "))
    while saving < 0:
        print("Por favor, escriba una cantidad positiva.")
        saving = float(input("¿Cuántos pesos quiere meter en la alcancia?: $ "))
    saved += saving

    print(f"Ahorro conseguido! Ha ahorrado usted {saved} pesos.")