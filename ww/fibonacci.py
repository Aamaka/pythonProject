count = int(input("enter number: "))
num1 = 0
num2 = 1
if count == 1:
    print(num2)
else:
    print(num1)
    print(num2)
    for i in range(2, count):
        result = num1 + num2
        num1 = num2
        num2 = result
        print(result)
