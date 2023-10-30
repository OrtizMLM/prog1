class Cuenta:
    def __init__(self, name, quantity): 
        self.__private_at = name
        self.__private_q = quantity

    @property
    def private_at(self):
        return self.__private_at
    @property
    def private_q(self):
        return self.__private_q
    
    @private_at.setter
    def private_at(self, new_at):
        self.__private_at = new_at
    @private_q.setter
    def private_q(self, new_q):
        self.__private_q = new_q
    
    def mostrar(self):
        print(f"El nombre es: {self.private_at} \nCuenta: {self.private_q}")
    
    def ingresar(self):
        cantidad = float(input("Dinero a ingresar: "))
        if cantidad > 0:
            self.private_q += cantidad
            print(self.private_q)
    def retirar(self):
        count = float(input("Dinero a retirar: "))
        self.private_q -= count
        print(f"El saldo quedo en: {self.private_q}")