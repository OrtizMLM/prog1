#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’.
from dic import *

while True:
    name = str(input("Ingrese nombre: "))
    age = str(input("Ingrese edad: "))
    phone = str(input("Ingrese telefono: "))
    dir = str(input("Ingrese direccion: "))
    
    dic(name, age, phone, dir)