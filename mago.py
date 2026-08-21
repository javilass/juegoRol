from personaje import Personaje #porque el mago es un hijo de personaje

class Mago(Personaje):
    def __init__(self, nombre, nivel, vida, poder_magico): #añadimos el poder mágico como atributo dle mago
        super().__init__(nombre, nivel, vida) #cuando ves "super" significa que te estás trayendo toda la hernecia de atributos
        self.poder_magico = poder_magico
        
#Polimorfismo:
    def atacar(self):
        print(f"{self.nombre} lanza un hechizo con {self.poder_magico} pts. de poder mágico")
        
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza Bola de Fuego")
        
        