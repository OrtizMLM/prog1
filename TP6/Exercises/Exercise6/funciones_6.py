

#   Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.

def show (p,s):

    for n in p|s:

        print(n)

#   Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.

def repeat (p,s):

    for n in p & s:
       
        print(n)

#   Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def no_repeat (p,s):

    for n in p - s:

        print(n)