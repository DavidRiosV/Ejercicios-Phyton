class Animal:
    def __init__(self, especie="", mensaje=""):
        self.especie = especie
        self.mensaje = mensaje
        
    def hablar(self):
        print(self.mensaje)

class Perro(Animal):
    def __init__(self):
        super().__init__(especie="perro", mensaje="Guau")


class Gato(Animal):
    def __init__(self):
        super().__init__(especie="gato", mensaje="Miau")

