class Rectangulo():

    def __init__(self,ancho="",altura=""):
        self.ancho=ancho
        self.altura=altura
        
    def area(self):
        return float(self.ancho)*float(self.altura) 
    
    def perimetro(self):
        return (2*(float(self.ancho)))*(2*(float(self.altura)))
    