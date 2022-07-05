number1 = int(input("enter a number: "))
number2 = int(input("enter a number: "))
number3 = int(input("enter a number: "))

total = number1 + number2 + number3
average = total / 3
product = number1 * number2 * number3

smallest = number1
if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3

largest = number1
if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3

print(total, "is the total sum ")
print(average, "is the average")
print(product, "is the product")
print(smallest, "is the smallest number")
print(largest, "is the largest")

