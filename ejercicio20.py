#Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el salario anual del empleado.
# Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.

from Empleado import *   

empleado1=Empleado("Jose",1200)
gerente1=Gerente("Paco",1300,50)
programador1=Programador("Ismael",1500,"java")

empleado1.calcular_salario_anual()
gerente1.calcular_salario_anual()
programador1.calcular_salario_anual()
programador1.lenguaje()

