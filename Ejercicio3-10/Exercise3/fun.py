def uploadPartners(partners):
   number=int(input("Número de socio (0 para cortar): "))
   while number!=0:
       name=input("Nombre y apellido: ")
       date=input("Fecha de ingreso (DDMMAAAA): ")
       subscription=input("¿Cuota al día? s/n: ")
       partners[number]=[name,date,subscription.lower()=="s"]
       number=int(input("Número de socio (0 para cortar): "))
   return partners

 
def modifyDate(partners, last_date, new_date):
   for data in partners.values():
       if data[1]==last_date:
           data[1]=new_date
   return partners

 
def number_Partner(partners, name):
   for number,data in partners.items():
       if data[0].lower()==name.lower():
           return number
   return 0

 
def format_date(date):
   return date[:2]+"/"+date[2:4]+"/"+date[4:]

 
def printList(partners):
   for number,data in partners.items():
       print("-Número:",number)
       print("-Nombre:",data[0])
       print("-Ingresó:", format_date(data[1]))
       if data[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

 
active_partners={1:["Ailen Bossio","09102023",True], 2:["Mauro Ortiz","10072023",True], 3:["Nicolas Barzola","05071994",True]}

 
print("***Cargar socios")
active_partners=uploadPartners(active_partners)

 
print("El club tiene", len(active_partners), "socios")

 
print("***Registrar pago de cuota")
number=int(input("Número de socio: "))
active_partners[number][2]=True

 
print("***Modificando fecha de ingreso...")
active_partners=modifyDate(active_partners, "09102023", "10072023")

 
print("***Eliminar socio")
name=input("Nombre y apellido: ")
number=number_Partner(active_partners, name)
if number in active_partners:
    del active_partners[number]

 
printList(active_partners)