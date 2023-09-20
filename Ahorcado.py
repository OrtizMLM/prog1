import random
# FUNCIONES
def word(): # FUNCION QUE ASIGNA UNA PALABRA Y GENERA GUIONES
    list = ["programa", "computadora", "funciones", "alumnos"]
    num = random.randint(0, len(list)-1)
    wor = list[num] # IGUALO A LA VARIABLE UNA PALABRA DE LA LISTA
    guide = ""
    for i in wor:
        guide += " _" # GENERO LOS GUIONES SEGUN LOS CARACTERES DE LA PALABRA
    tex = str(input(f"Ingrese la primer letra: {guide}"))
    words = check(wor, tex, guide) # ENVIO PARAMETROS
    return wor

def check(wor, tex, gio): # FUNCION QUE CHEQUEA CARACTERES INGRESADOS POR USUARIO
    i = 0 # VALOR PARA RECORRER CADA CARACTER
    att = 6 # VALOR DE INTENTOS
    key = "" 
    while att > 0:
        if tex.lower() == wor[i]:
            print("ADIVINASTE!")
            key += tex.lower() # VARIABLE PARA AGREGAR CARACTERES ADIVINADOS
            i += 1
            gio = gio.replace(" _", "", 1) # REEMPLAZO GUIONES POR VACIO
            tex = str(input(f"/ INTENTOS: {att} / Ingrese la proxima letra: {key}{gio}"))
            if i == (len(wor)-1): 
                print("FELICITACIONES COMPLETASTE TODA LA PALABRA !!!") # MENSAJE UNA VEZ QUE SE ADIVINA LA PALABRA COMPLETA
                break
        else:
            att -= 1 # RESTO UN INTENTO
            tex = str(input(f"FALLASTE! Intentalo de nuevo! / INTENTOS: {att} / Ingrese la proxima letra: {key}{gio}"))
            continue
    print("AGOTASTE TODOS LOS INTENTOS!") # UNA VEZ AGOTADOS TODOS LOS INTENTOS

# MAIN
word()
