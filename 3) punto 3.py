def PrimosOno(a):
    cont=0
    contP=0
    while cont <= a :
        cont += 1
        if a % cont == 0:
            contP += 1

    if  contP>2:
            print("no es primo")
    else:
            print("si lo es")

a=int(input("Numero a evaluar: "))
PrimosOno(a)