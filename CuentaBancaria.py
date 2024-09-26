class CuentaBancaria():

    def __init__(self,titular="",saldo=0.0):
        self.titular=titular
        self.saldo=saldo

    
    def depositar(self, ingreso):
        self.saldo = self.saldo + ingreso
        print("Su saldo ahora es de " + str(self.saldo))
    
    def retirar(self, retiro):
        self.saldo = self.saldo - retiro
        print("Su saldo ahora es de " + str(self.saldo))

