sum=0

for grade in range(3):
    grade=float(input("enter a grade(from 1.0 to 5.0): "))
    sum += grade

average = sum/3
print("your average is: ", average)
if average >=3.0:
    print("aproved")
else:
    print("Reproved")