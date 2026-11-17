num=int(input("adivina el numero del uno al diez:"))
numerocor=7

while num!=numerocor:
    if num<numerocor:
        print("el numero es mayor")
    else:
        print("el numero es menor")
    num=int(input("adivina el numero del uno al diez:"))

print("felicidades adivinaste el numero es 7")