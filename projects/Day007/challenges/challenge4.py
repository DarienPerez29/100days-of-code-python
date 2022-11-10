# Step 4

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = len(stages) - 1

# Testing code
print(f'Psst, the solution is {chosen_word}.')

display = []
for l in chosen_word:
    display.append("_")

out = False
while (not out):
    guess = input("Guess a letter: ").lower()

    # Change display if letter guessed is founded
    for i, l in enumerate(chosen_word):
        if l == guess:
            display[i] = l
    
    if guess not in chosen_word:
        lives -= 1

    print(' '.join(display))
    print("\n" + stages[lives])

    if "_" not in display: 
        out = True
        print("\nYou win!!!")
    elif lives == 0:
        out = True
        print("\nYou loose :C")
        

