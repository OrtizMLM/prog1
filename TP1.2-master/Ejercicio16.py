#"Trabajo practico 1.2"
#Ejercicio 16
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Ingrese el nombre: ") #Pido los datos al usuario.
apellido1 = input("Ingrese el primer apellido: ")
apellido2 = input("Ingrese el segundo apellido: ")

inicialNombre = nombre[0] #Extraigo el primer valor de cada cadena.
inicialPrimApe = apellido1[0]
inicialSegundoApe = apellido2[0]

print ("Inicial del nombre: " + inicialNombre) #Muestro los valores.
print ("Inicial del primer apellido: " + inicialPrimApe)
print ("Inicial del segundo apellido: " + inicialSegundoApe)