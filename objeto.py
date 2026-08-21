class Objeto:
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def mostrar_informacion(self):
        print(f"Objeto{self.nombre}")
        print(f"Objeto{self.tipo}")
        
        