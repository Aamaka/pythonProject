import random

my_list = ["Lie", "Ada", "Obi", "James", "Hope", "Joy", "Tip", "lock", "unlock", "growth"]

chosen_word = random.choice(my_list)
word_len = len(chosen_word)
display = []

for _ in range(word_len):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("guess a word: ").lower()

    for position in range(word_len):
        word = chosen_word[position]
        if word == guess:
            display[position] = word
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
