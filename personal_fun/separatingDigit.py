number = (input("Enter 5 number:  "))

for n in number:
    print(n, end=" ")

if number[0] == number[4] and number[1] == number[3]:
    print("palindrome")

else:
    print("not a palindrome")

num = int(input("Enter the length: "))

for n in range(num):
    for j in range(n + 1):
        print("*", end=" ")
    print()

print()

for n in range(num):
    for j in range(n, num):
        print("*", end=" ")
    print()
