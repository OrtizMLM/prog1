#Escriba un programa que pida el año actual y
# un año cualquiera y que escriba cuántos años han pasado desde ese año 
#o cuántos años faltan para llegar a ese año.

an_actual = int(input("Ingrese el año actual: "))
an_cualq = int(input("Ingrese otro año cualquiera: "))

if an_actual > an_cualq :
    diferencia = an_actual - an_cualq

    print(f"Han pasado {diferencia} años desde el {an_cualq}")

elif an_actual < an_cualq :
    faltante = an_cualq - an_actual

    print(f"Faltan {faltante} años para el año {an_cualq}")