#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico.
# Luego, crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.
from InstrumentoMusical import *   

bombo=InstrumentoMusical()
piano1=Piano()
guitarra1=Guitarra()

bombo.tocar()
piano1.tocar()
guitarra1.tocar()

