def PotencaiDeUnaBase(a,b):
    Resultado=a**b
    print("El reslutado es ",Resultado )
a=float(input("Valor a ingresar como base: "))
b=float(input("valor a ingresar como ingresara como potencia: "))
c=float(input("Siguiente base: "))
d=float(input("Siguiente potencia: "))
x1=a**b
x2=c**d
PotencaiDeUnaBase(a,b)

PotencaiDeUnaBase(c,d)
if x1>x2:
     print("la primera potencia es mayor: ")
else:
     print("la segunda potencia es menor: ")