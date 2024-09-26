#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. 
# Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal 
# y sobrescriban el método hablar para imprimir mensajes diferentes.
from Animal import *   

animal1=Perro() 

animal2=Gato()

animal3=Animal("pez","Gluglu")

animal1.hablar()
animal2.hablar()
animal3.hablar()