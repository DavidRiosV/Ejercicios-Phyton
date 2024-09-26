#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. 
#Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica 
#y sobrescriban el método area para calcular el área específica de cada figura.
from FiguraGeometrica import *   

Circulo=FiguraGeometrica(2,5,0)
Circulo=Rectangulo(2,5) 
Circulo=Triangulo(2,5)

Rectangulo.area()
Triangulo.area()
