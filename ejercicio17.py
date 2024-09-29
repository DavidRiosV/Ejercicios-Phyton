#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. 
#Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica 
#y sobrescriban el método area para calcular el área específica de cada figura.
from FiguraGeometrica import *   

figura1=FiguraGeometrica(12,2)
rectanfulo1=Rectangulo(10,5) 
triangulo1=Triangulo(2,5)

print(figura1.area())
print(rectanfulo1.area())
print(triangulo1.area())