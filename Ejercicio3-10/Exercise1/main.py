from add import *
from city import *


def main():
    pas = []
    cit = []
    while True: 
        option = int(input(" \n/// INGRESE UN NUMERO PARA INGRESAR A UNA OPCION /// \n(1) Agregar pasajeros a la lista: \n(2) Agregar ciudades a la lista: \n(3) Consultar por DNI ver ciudad: \n(4) Consultar por ciudad ver cantidad de pasajeros: \n(5) Consultar por DNI ver pais: \n(6) Consultar por pais cuantos pasajeros viajan: \n(7) Salir del programa: \n"))
        if option == 1:
            city = add()
            tup = (city[2], city[3])
            cit.append(tup)
            pas.append(city)
        if option == 2:
            tp = ci()
            cit.append(tp)
            print(cit)
        if option == 3:
            dn = str(input("Ingrese DNI a consultar: "))
            for tupla in pas:
                if dn in tupla:
                    print(f"El pasajero con el DNI:{dn}. Viaja a la ciudad: {tupla[2]}")
                else:
                    print("Ninguno pasajero encontrado con ese DNI.")
        if option == 4:
            ct = str(input("Ingrese ciudad a consultar: "))
            pasa = 0
            for tupla in pas:
                if ct in tupla:
                    pasa += 1
            print(f"La cantidad de pasajeros que viajan a {ct} son: {pasa}")
        if option == 5:
            dn = str(input("Ingrese DNI a consultar: "))
            for tupla in pas:
                if dn in tupla:
                    print(f"El pasajero con el DNI:{dn}. Viaja al pais: {tupla[3]}")
                else:
                    print("Ninguno pasajero encontrado con ese DNI.")
        if option == 6:
            cn = str(input("Ingrese pais a consultar: "))
            pasa = 0
            for tupla in pas:
                if cn in tupla:
                    pasa += 1
            print(f"La cantidad de pasajeros que viajan a {cn} son: {pasa}")
        if option == 7:
            break

main()