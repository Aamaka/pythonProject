numberOfSteps = 4
a = [2, 4, 5, 67, 8, 9]

for i in range(numberOfSteps):
    j = a.pop()
    a.insert(0, j)
    print(a)
