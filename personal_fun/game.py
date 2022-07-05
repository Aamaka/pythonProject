import random

user_input = int(input("enter 0 for scissors , 1 for rock  and 2 for paper: "))

computer_input = random.randint(0, 2)


if user_input == 0:
    user_input = "scissors"
elif user_input == 1:
    user_input = "rock"
else:
    user_input = "paper"

if computer_input == 0:
    computer_input = "scissors"
elif computer_input == 1:
    computer_input = "rock"
else:
    computer_input = "paper"

if computer_input == 0 and user_input == 0:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer played scissors as well it "
          f"is a draw")
elif computer_input == 0 and user_input == 1:
    print(f"The computer played {computer_input} and you played {user_input}.\nPlayer wins!!! ")
elif computer_input == 0 and user_input == 2:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer wins!!!")
elif computer_input == 1 and user_input == 0:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer WIns!!!")
elif computer_input == 1 and user_input == 1:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer played rock as well it is a "
          f"draw")
elif computer_input == 1 and user_input == 2:
    print(f"The computer played {computer_input} and you played {user_input}.\nPlayer wins!!!")
elif computer_input == 2 and user_input == 0:
    print(f"The computer played {computer_input} and you played {user_input}.\nPlayer wins!!!")
elif computer_input == 2 and user_input == 1:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer wins!!!")
else:
    print(f"The computer played {computer_input} and you played {user_input}.\nComputer played paper as well it is a "
          f"draw")

