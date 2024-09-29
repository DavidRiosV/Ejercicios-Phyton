class Vehiculo():
    
    def __init__(self,marca="",modelo=""):
        self.marca=marca
        self.modelo=modelo
        
    def informacion(self):
        print("Marca: "+str(self.marca) +"Modelo: "+str(self.modelo)+".")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
    
    def informacion(self):
        return "Marca:" +str(self.marca) +"/Modelo:"+str(self.modelo) +"/Color:"+str(self.color)+"."
    
    def aparcar(self):
        return "El coche esta aparcado."

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
    
    def informacion(self):
        return "Marca:" +str(self.marca) +"/Modelo:"+str(self.modelo) +"/Color:"+str(self.color)+"."
    
    def pedalear(self):
        return "Estás pedaleando la bicicleta."