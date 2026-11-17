num = int(input("Ingrese un número hasta el cual quieras sumar:"))
total = 0

for num in range (1, num+1):
    total += num

print("La suma de los números desde 1 hasta", num, "es:", total)