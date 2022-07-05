radius = 2
pi = 3.14

diameter = 2 * (radius * 2)
circumference = 2 * radius * pi
area = pi * (radius * 2)
print(diameter, circumference, area)


number = int(input("enter a number: "))
if number % 2 == 0:
    print("its even")
else:
    print("its odd")


numbers = 1024
if numbers % 4 == 0:
    print("it's a multiple")
else:
    print("not a multiple")

if 10 % 2 == 0:
    print("yes")
else:
    print("no")

counter = 0

print("counter   square    cubes\n")
for counter in range(0, 6):
    square = counter * counter
    cubes = counter * counter * counter

    print(f"""
{counter}           {square}            {cubes}
    """)
