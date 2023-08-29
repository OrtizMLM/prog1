voto = str(input("Digite el candidato elegido: | 'A' PARTIDO ROJO | 'B' PARTIDO VERDAD | 'C' PARTIDO AZUL : "))
if voto.lower() == "a":
    print("Usted a votado por el Partido Rojo")
elif voto.lower() == "b":
    print("Usted a votado por el Partido Verdad")
elif voto.lower() == "c":
    print("Usted a votado por el Partido Azul")
else:
    print("Opcion erronea")