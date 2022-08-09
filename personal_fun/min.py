myList = [1, 3, 5, 7, 9]


def maxi(m):
    maximum = max(m)
    maxim = sum(m) - maximum
    print(maxim)


maxi(myList)


def mini(m):
    minimum = min(m)
    minim = sum(m) - minimum
    print(minim)


mini(myList)
