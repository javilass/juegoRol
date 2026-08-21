from personaje import Personaje #porque el guerrero es un hijo de personaje

class Guerrero(Personaje):
    def __init__(self, nombre, nivel, vida, fuerza): #añadimos fuerza como atributo del guerrero
        super().__init__(nombre, nivel, vida) #cuando ves "super" significa que te estás trayendo toda la hernecia de atributos
        self.fuerza = fuerza
        
#Polimorfismo:
    def atacar(self):
        print(f"{self.nombre} lanza un golpe con {self.fuerza} pts. de fuerza")
        
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza Golpe de espada")
        
        