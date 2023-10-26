from Moto import Moto


moto1 = Moto(1,"Naranja",'AD-EE',"nafta",10,2023,'25/12/2022',200,150)
moto2 = Moto(2,"Roja",'AD-E1',"nafta",12,2023,'29/12/2022',210,170)
# while True:
    # id = int(input("Ingrese id de la moto: "))
    # action = int(input(f"Seleccione una accion: 1- Arrancar motor \n 2- Detener motor"))
    # if action == 1:
    #     moto1.arrancar()
    # elif action == 2:
    #     moto1.detener()
    # else:
    #     break      
moto1.price = 2000
print(f"La moto 1 vale {moto1.price}")

moto1.mostrarPrecio()
moto2.mostrarPrecio()