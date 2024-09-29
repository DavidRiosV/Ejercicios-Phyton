class FiguraGeometrica():
    def __init__(self, ancho=0, altura=0):
        self.ancho = ancho
        self.altura = altura
        
    def area(self):
        return "No tiene area asignada"
        
class Rectangulo(FiguraGeometrica): 
        def area(self):
            return "El area del rectangulo es " +str(self.ancho * self.altura)

class Triangulo(FiguraGeometrica):
        def area(self):
            return "El area del triangulo es " +str((self.ancho*self.altura)/2)
    
        
        