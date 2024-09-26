#Crea una clase llamada CuentaBancaria con atributos titular y saldo.
# Agrega métodos para depositar y retirar dinero de la cuenta.
from CuentaBancaria import *

CuentaBancaria1=CuentaBancaria("Paco",2000)
CuentaBancaria2=CuentaBancaria("Ana",3000)
CuentaBancaria3=CuentaBancaria("Vanesa",6000)

CuentaBancaria1.depositar(50)
CuentaBancaria2.retirar(30)
CuentaBancaria3.retirar(6000)
