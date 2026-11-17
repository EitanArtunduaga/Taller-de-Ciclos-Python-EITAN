palabra = ""
 
while palabra != "salir":
    palabra = input("Escribe 'hola' o 'salir': ")
    if palabra == "hola":
        print("como estas?")
    elif palabra != "salir":
        print("palabra incorrecta")
 
print("adios")
