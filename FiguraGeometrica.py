class FiguraGeometrica():
        def __init__(self, ancho="", altura="",area=0.0):
        self.ancho = ancho
        self.altura = altura
        
    def area(self,area):
        print(str(area))
        
class Rectangulo(FiguraGeometrica): 
        def __init__(self):
        super().__init__(area=self.ancho*self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__(area=(self.ancho*self.altura)/2)
    
        
        