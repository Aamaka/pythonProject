print("input numbers from 1 - 100: ")
number = 20
counter = 1

while counter <= 3:
    guess = int(input("Enter number: "))
    if guess == number:
        print("you are correct")

    elif guess > number:
        print("too high")

    else:
        print("too low")
    counter += 1

# guess = int(input("enter a number: "))
#
# number = 12
#
# for i in range(1, 3):
#     if guess == number:
#         print("you win")
#     elif guess > number:
#         print("too high")
#     else:
#         print("too low")
