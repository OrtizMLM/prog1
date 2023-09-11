# Ejercicio 11
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo 
#de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
#le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de 
#la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza 
#elegida es vegetariana o no y todos los ingredientes que lleva.

vege = str(input("Desea que su pizza sea vegetariana? s/n: "))

if vege.lower() == "s":
        ingre = str(input("Seleccione el ingrediente (Pimiento o Tofu): "))
        if ingre == "Pimiento" or ingre == "Tofu":
            print (f"La pizza vegetariana se prepara con los siguientes ingredientes: mozzarella, tomate y {ingre}")
        else:  
            print("Ingrese los ingredientes correctamente")
else:
        ingre = str(input("Seleccione el ingrediente (Peperoni, Jamon y Salmon): "))
        if ingre == "Peperoni" or ingre == "Jamon" or ingre == "Salmon":
            print (f"La pizza vegetariana se prepara con los siguientes ingredientes: mozzarella, tomate y {ingre}")
        else:  
            print("Ingrese los ingredientes correctamente")
        
