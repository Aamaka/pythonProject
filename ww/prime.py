import math
number = int(input("enter a number: "))
x = math.sqrt(number)
y = math.ceil(x)
begin = 2
while begin <= y:
    begin += 1
if number % begin == 0:
    print(number, "is not a prime number")

else:
    print(number, "is a prime number")
