#Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo.
# Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo
from Vehiculo import *   

coche = Coche("Toyota", "Corolla", "Gris")
bicicleta = Bicicleta("Trek", "FX 3", "Roja")

print("")
print(coche.informacion())
print(coche.aparcar())
print("")
print(bicicleta.informacion())
print(bicicleta.pedalear())