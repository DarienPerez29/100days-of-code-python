# Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Psst, the solution is {chosen_word}.')

display = []
for l in chosen_word:
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
out = False
while(not out):
    guess = input("Guess a letter: ").lower()

    for i, l in enumerate(chosen_word):
        if l == guess:
            display[i] = l

    for l in display:
        print(l, end = "")

    if "_" in display: out = False
    else: out = True

    print("\n")

print("Game over")
