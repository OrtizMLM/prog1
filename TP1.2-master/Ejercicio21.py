#"Trabajo practico 1.2"
#Ejercicio 21

#Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.


kmxlitro = int(input("Ingrese la cantidad de kilometros por litro que consume la moto: ")) #Ingreso valores necesarios
capacidad = int(input("Ingrese la cantidad de litros maximos del tanque: "))
kmrecorrer = int(input("Cantidad de km a recorrer: "))

kmxtanque = kmxlitro * capacidad #Calculo la cantidad de tanques necesarios
tanques = kmrecorrer / kmxtanque

print ("La cantidad de tanques necesarios para el viaje son: " + str(tanques)) #Muestro los tanque necesarios


