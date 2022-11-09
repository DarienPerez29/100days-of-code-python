# Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Psst, the solution is {chosen_word}.')

#TODO_1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'
display = []
for l in chosen_word:
    display.append("_")

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word
#If the letter at that position matches 'guess', then reveal that letter in the display at that position
for i, l in enumerate(chosen_word):
    if l == guess:
        display[i] = l

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
for l in display:
    print(l, end = "")