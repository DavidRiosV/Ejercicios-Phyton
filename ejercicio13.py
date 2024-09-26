#Crea una clase llamada Estudiante con atributos nombre, edad y curso.
#Crea varios objetos de tipo Estudiante y almacénalos en una lista. 
#Luego, itera sobre la lista e imprime la información de cada estudiante.
from Estudiante import *

Estudiante1=Estudiante("Paco","14","2ºC")
Estudiante2=Estudiante("Jose","22","2ºDAW")
Estudiante3=Estudiante("Maria","30","1ºSMR")

lista_estudiantes = [Estudiante1, Estudiante2, Estudiante3]

for i in lista_estudiantes:
    print(i.nombre,i.edad,i.curso)