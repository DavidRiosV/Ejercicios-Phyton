#Calcula el factorial de un número.
print("Ingresa el numero del cual quieres saber su factorial")
n = input()
f =1
for n in range(int(n),1,-1):
    f=int(n)*int(f)
print("El factorial es "+str(f))
