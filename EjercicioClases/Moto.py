class Moto:
    motor = False
    state = 'new'
    def __init__(self, id,color, matricula, oil_lt, n_ruedas, model, fecha_fab, vel_pun, peso):
        self.id = id
        self.color = color
        self.matricula = matricula
        self.oil_lt = oil_lt
        self.n_ruedas = n_ruedas
        self.model = model
        self.fecha_fab = fecha_fab
        self.vel_pun = vel_pun
        self.peso = peso
    def detener (self):
        if self.motor == True:
            self.motor = False
            print("El motor se detuvo")
        else:
            print("El motor ya esta detenido.")
    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print("El motor se arranco")
        else:
            print("El motor ya esta arrancado.")
    def mostrarPrecio(self):
        print(f"La moto 1 vale {self.price}")