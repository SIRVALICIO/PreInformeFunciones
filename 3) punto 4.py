
def primoHermano(a):
    cont=0
    contP=0
    if a%6==0 or a==6:
        print("numero no valido")
    else:
        while cont<=a+1:
            cont+=1
            if (a+1)%cont==0:
                contP+=1

        if contP>2 :

            print("No es primo hermano")

        else:
            print("si lo es")



a=int(input(" numero deseado a evalar: "))
primoHermano(a)