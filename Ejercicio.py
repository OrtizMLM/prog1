import time
fecha = input("Ingrese fecha en formato 'dia, DD/MM': ")
diaSem = str(fecha[0:fecha.find(',')])
diaSem = diaSem.lower()
dia = int(fecha[fecha.find(' ')+1:fecha.find('/')])
mes = int(fecha [fecha.find('/')+1:])
var = (str(diaSem) + str(dia) + str(mes))


if (diaSem != "lunes" and diaSem != "martes" and diaSem != "miercoles" and diaSem !="jueves" and diaSem !="jueves" and diaSem !="viernes") or dia > 31 or mes > 12: 
    print ("SE PRODUJO UN ERROR")
else:
    print (f"El día {diaSem} {dia} del {mes}")
    if  diaSem in "lunes,martes,miercoles":
        resp = str(input("Se tomaron examenes? s/n: "))
        if resp.lower() == "s":
            apro = int(input("ingrese la cantidad de aprobados: "))
            desa = int(input("Ingrese la cantidad de desaprobados: "))
            print(f"El promedio de aprobados es el {(apro*100)/(apro+desa)}%")
    if diaSem == "jueves":
        porcentaje = int(input("Ingrese el porcentaje de asistencia: "))
        if porcentaje > 50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    if diaSem == "viernes" and ((mes == 1 or mes == 7) and dia == 1):
        cantAlum = int(input("Comienzo de nuevo ciclo! Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = int(input("Arancel por alumno: "))
        print(f"Ingreso total: ${(cantAlum*arancel)}")

print("------------------- FIN DEL PROGRAMA --------------------------------")
time.sleep(5)
