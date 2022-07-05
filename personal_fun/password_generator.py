import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

sign = ['@', '!', '#', '$', '%', "^", '&', '*', '<', '>', ",", '.', '/']

alphanum = int(input("number of alphabet : "))
num_num = int(input("number of numbers : "))
sign_num = int(input("number of signs : "))

password_list = []

for alphabet in range(alphanum):
    password_list.append(random.choice(alpha))

for number in range(num_num):
    password_list.append(random.choice(num))

for symbol in range(sign_num):
    password_list.append(random.choice(sign))


random.shuffle(password_list)
print(password_list)
for pasa in password_list:
    print(pasa, end="")