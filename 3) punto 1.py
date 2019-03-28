def ConteoDeImparesc(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
n=int(input("digite un entero que quiera conteaar"))
ConteoDeImparesc(n)

a=input("quiere voler a intentarlo? y/n: ")
if a=="y":
    while a!="n":
        b=int(input("Nuevo valor a evaluar: "))
        ConteoDeImparesc(b)
        a=input("quiere seguir? y/n: ")
        if a=="n":
            print("muchas gracias")

