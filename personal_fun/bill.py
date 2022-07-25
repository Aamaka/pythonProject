import random

seed = input("enter your seed number: ")
random.seed(seed)

name = input("Enter everybody's name separated with a comma: ")
names = name.split(",")
print(names)
n = len(names)
k = random.randint(0, n - 1)

bill = names[k]
print(bill + " will pay the bill")
