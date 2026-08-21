class Inventario:
    
    def __init__(self):
        self.objetos = []
        
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
        print(f"{objeto.nombre} ha sido agregado al inventario")
        
    def mostrar_inventario(self):
        print("\n ---Inventario---")
        if len(self.objetos) == 0: #Validamos si hay objetos en el inventario
            print("El inventario está vacío")
        else:
            for objeto in self.objetos: #Recorro la lista de objetos
                print(f"- {objeto.nombre} ({objeto.tipo})") #Imprimo cada objeto y su tipo
                
                