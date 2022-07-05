num = int(input("enter number: "))
total = 0
for i in range(1, num+1):
    total += i
print(total)

product = 1
for i in range(1, num+1):
    product *= i
print(product)

a, b = 0, 1

while a < num:
    print(a)
    a, b = b, a + b


smiley = "\U0001f600"
for i in range(1, 21, 2):
    print(f"{smiley * i:>20}")

smiley = "\U0001f601"
for i in range(1, 21, 2):
    print(f"{smiley * i:>20}")

star = "*"
for i in range(1, 11):
    print(f"{star * i:<10} {star * (11-i):<10}  {star * (11-i):>10} {star * i:>10} ")
