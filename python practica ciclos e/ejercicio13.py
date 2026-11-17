conteo = input("Escribe una palabra: ")
vocales = 0
 
for l in conteo.lower():
    if l in "aeiou":
        vocales += 1
 
print("tu palabra tiene ", vocales, " vocales")
