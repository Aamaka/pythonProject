number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))

largest = number1
if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3


smallest = number1
if number2 < smallest:
    smallest = number2

if number3 < smallest:
    smallest = number3

print(" ")
print("largest is ", largest)
print("smallest is ", smallest)
