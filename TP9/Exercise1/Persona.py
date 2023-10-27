class Persona:
    def __init__(self, name='', age=0, dni=0):
        self.__private_at = name
        self.__private_a = age
        self.__private_d = dni
    
    @property
    def private_at(self):
        return self.__private_at
    @property
    def private_a(self):
        return self.__private_a
    @property
    def private_d(self):
        return self.__private_d
    
    @private_at.setter
    def private_at(self, new_at):
        self.__private_at = new_at
    @private_a.setter
    def private_a(self, new_a):
        self.__private_at = new_a
    @private_d.setter
    def private_d(self, new_d):
        self.__private_at = new_d

    

    def esMayorDeEdad (self):
        if self.private_a >= 18:
            may = True
            return(may)
        else:
            may = False
            return(may)
    def mostrar(self):
        print(f"El nombre de la Persona es: {self.private_at} \n La edad es: {self.private_a} \n El DNI es: {self.private_d}")
