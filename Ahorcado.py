import random
# FUNCIONES
def word(): # FUNCION QUE ASIGNA UNA PALABRA Y GENERA GUIONES
    list = ["programa", "computadora", "funciones", "alumnos"]
    num = random.randint(0, len(list)-1)
    wor = list[num] # IGUALO A LA VARIABLE UNA PALABRA DE LA LISTA
    guide = [] # GENERO LISTA DE GUIONES
    for i in wor:
        guide.append('_') # GENERO LOS GUIONES SEGUN LOS CARACTERES DE LA PALABRA
    check(wor, guide) # ENVIO PARAMETROS
    return wor

def check(wor, gio): # FUNCION QUE CHEQUEA CARACTERES INGRESADOS POR USUARIO
    att = 6 # VALOR DE INTENTOS
    worok = [] # LISTA DE LETRAS INCORRECTAS
    while True:
        tex = str(input(f"Ingrese una letra: ").lower())
        
        if tex in worok: # CHEQUEO SI LA LETRA YA FUE INGRESADA
            print("YA INGRESASTE ESA LETRA. INTENTA CON OTRA! ")
            continue 
        if tex not in wor: # CHEQUEO SI LA LETRA ES INCORRECTA
            att -= 1
            worok.append(tex)
            print(f"Letra incorrecta. Te quedan {att} INTENTOS.")
        
        else:   
            for i in range(len(wor)): # SI LA LETRA INGRESADA ES CORRECTA LA REEMPLAZO EN LA LISTA DE GUIONES
                    if wor[i] == tex:
                        gio[i] = tex
        print("Palabra: " + " ".join(gio))
        print("Letras INCORRECTAS: " + ", ".join(worok))

        if '_' not in gio: # CHEQUEO SI YA ADIVINO TODA LA PALABRA
            print(f"Felicitaciones adivinaste la palabra: {wor.upper()}")
            break
        if att == 0: #CHEQUEO LOS INTENTOS
            print(f"AGOTASTE TODOS LOS INTENTOS! LA PALABRA ERA: {wor.upper()}")
            break
# MAIN
word()