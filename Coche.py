class Coche():
    
    def __init__(self,marca="",modelo=""):
        self.marca=marca
        self.modelo=modelo
        
    def informacion(self):
        print("La marca del coche es "+str(self.marca) +" y el modelo es "+str(self.modelo)+".")