class Empleado():
    
    def __init__(self,nombre="",salario=0):
        self.nombre=nombre
        self.salario=salario
        
    def calcular_salario_anual(self):
        print("El salario de "+self.nombre +" es de " +str((self.salario)*12))

class Gerente(Empleado):
     def __init__(self, nombre, salario, extra):
         super().__init__(nombre, salario)
         self.extra = extra
         
     def calcular_salario_anual(self):
            print("El salario de "+self.nombre +" es de " +str(((self.salario)*12)+self.extra))

class Programador(Empleado):
     def __init__(self, nombre, salario, idioma):
        super().__init__(nombre, salario)
        self.idioma = idioma
        
     def lenguaje(self):
            print(self.nombre +" programa en " +self.idioma)
