suma = 0
cantidad = 0
nota = float(input("Nota(escribe -1 para finslizar): "))
 
while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("Nota(escribe -1 para finalizar): "))
 
if cantidad > 0:
    print("Promedio", suma / cantidad)
else:
    print("No hay notas")
