import random
import hang

my_list = ["Lie", "Ada", "Obi", "James", "Hope", "Joy", "Tip", "lock", "unlock", "growth"]

lives = 6
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

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hang.stages[lives])
