import random

random_int = random.random() * 5
print(random_int)

rand = random.randint(0, 1)
if rand == 1:
    print("Heads")
else:
    print("Tails")
    

r = random.randrange(0, 11, 2)
print(r)


#
# t = (7, "nut", 9, 7)
# print(t)
#
# print(t.count(7))
# print(t.index(2, 1, 3))
