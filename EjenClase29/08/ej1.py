alfabeto ="abcdefghijklmnñopqrstuvwxyz"
especial = "!¡?¿."
corrimiento = int(input("Corrimiento: "))
for i in range(1):    
    mensaje = input("Escribe el mensaje a incriptar: ")    
    encriptado = "" 
    encriptado2 =""   
    for caracter in mensaje:        
        if caracter.lower() in alfabeto:           
            codigo = alfabeto.find(caracter.lower())         
            codigo = (codigo+corrimiento)%27         
            encriptado += alfabeto[codigo]
    for caracter2 in mensaje :
        if caracter2 in especial :
            esp = especial.find(caracter2.lower())
            encriptado2 += especial[esp]

else:
    encriptado+caracter+encriptado2+caracter2
    print(f"su mensaje incriptado es: ¨{encriptado}{encriptado2}")