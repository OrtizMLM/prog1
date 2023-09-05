# 1. Cree un bucle while con las siguientes características: • El valor inicial de la variable x será 0.
# • El valor del incremento será 1. • La condición de salida del bucle será mayor o igual a 30. 
#• La ejecución debe romperse cuando x es igual a 15. 
#• Debe imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# • Debe omitir las ejecuciones con el valor de x en 4, 6 y 10. 
#• En cada salto de ejecución, debe mostrar los valores saltados con este mensaje: 'Se omitió el valor ' + x ' de x'. 
#• Cuando se rompe la ejecución del bucle, debe mostrar un mensaje que lo indique: 
#'La ejecución del bucle se rompió cuando x era ' + x.

x = 0

while x <= 30: 
    x += 1
    if x == 4 or x == 6 or x == 10:
        print("- Se omitió el valor de: ",x)
        continue
    if x == 15:
        print("La ejecucion se rompio cuando x es:",x)
        break
    print("El valor del bucle es: ",x)

    

    

