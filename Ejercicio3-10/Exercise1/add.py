def add():
    passen = str(input("Nombre y apellido del pasajero: "))
    dni = str(input("DNI del pasajero: "))
    country = str(input("Pais al que viaja: "))
    city = str(input(f"Ingrese a la ciudad de {country} que viaja: "))
    tup = (passen, dni, city, country)
    return tup
