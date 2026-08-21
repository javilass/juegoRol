from inventario import Inventario

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.edad = nivel
        self.vida = vida
        self.inventario = Inventario() #Cada personaje tendrá su propio inventario

    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")
        
    def recibir_danio(self,danio):
        self.vida -= danio #self.vida = self.vida - danio --> va a reemplazar con el nuevo nivel de vida
        if self.vida < 0:
            self.vida = 0 #La vida siempre debe quedar en 0, nunca en - algo
        print(f"{self.nombre} recibió {danio} puntos de daño. ")
        print(f"La vida actual es: {self.vida}")
        
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza una habilidad")
        
    def mostrar_informacion(self):
        print("\n ---Información del PJ---")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")

