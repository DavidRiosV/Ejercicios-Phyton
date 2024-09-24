#Crea una lista de números y calcula su promedio. 

#Creo una lista
lista = [10, 20, 30]

#creo un contador que me dira la cantidad de numeros de la lista
c = 0
#creo la variable suma
suma=  0

for i in lista:
    #incremento el contador por cada número
    c=c+1
    #realizo la suma de todos
    suma=suma+i

promedio=suma/c
print("El promedio es de "+str(promedio))