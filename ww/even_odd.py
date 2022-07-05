number = int(input("Enter number: "))
while number != 1:
    if number % 2 != 0:
        number = number * 3 + 1
    elif number % 2 == 0:
        number = number // 2
    print(number, end=" ")
print(" ")
for i in range(1, 11):
    print("*"*i)
print(" ")
for i in range(11, 0, -1):
    print("*"*i)
