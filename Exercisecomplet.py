# Este ejercicio se realiza en grupo, pero la entrega es individual.

# Crear un programa utilizando todo lo aprendido hasta el momento.

# Condicionales
# Iteraciones (for / while)
# Break / Continue

#Programa que muestre los estudiantes con su nota, ingresando ambos valores por unica vez y luego mostrando solo los aprobados.

students = []
note = []

option = int(input("1- Para continuar ingresando estudiantes. 2- Para salir: "))
while option != 2:
    student = str(input("Ingrese la nota seguido el nombre del alumno: "))
    if int(student[0:2]) in range(0, 10):
        students.append(student)
        n = (int(student[0:2]))
        note.append(n)
        print(note)
        print(students)
    else:
        print("Ingrese una nota correcta")
        break
    option = int(input("1- Para continuar ingresando estudiantes. 2- Para salir: "))

flag = 0
for i in note:
    if i > 6:
        flag += 1
print("Los aprobados son: ", flag)
