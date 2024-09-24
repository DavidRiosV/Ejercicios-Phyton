#Calcula el máximo común divisor (MCD) de dos números. 
print("Dime el primer numero")
n1 = input()
print("Dime el segundo numero")
n2 = input()

d = 0
if n1 >= n2:
   d = n1
else:
   d = n2

maxd = 0
for d in range (int(d), 1, -1):
   if int(n1) % d == 0 and int(n2) % d == 0:
       if d > maxd:
           maxd = d
           print("Maximo Comun Divisor es " +str(d))
