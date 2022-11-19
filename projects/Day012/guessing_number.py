import os
import art
import random

# Function to clear screen in windows or linux
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

number_to_guess = random.randint(1, 100) # Random number defined
mode = ""
lifes = 0
guess = 0
has_won = False

# Welcome messages
clear_screen()
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100\n")

# Mode selection
while True:
    mode = input("Chose a difficulty (easy/hard): ").lower()
    
    if mode == "easy":
        lifes = 10
        break
    elif mode == "hard":
        lifes = 5
        break
    else:
        print("\nPlease select a valid option...")

# Guessing section
while True:
    clear_screen()
    
    if lifes >= 1: # Flow if player still has lifes
        print(f"\nYou have {lifes} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lifes -= 1

        if guess < number_to_guess:
            print(">>> Too low <<<")
        elif guess > number_to_guess:
            print(">>> Too high <<<")
        else:
            has_won = True
            break
        
        if lifes > 0:
            print("Guess again...")

    else: # Run out of lifes
        break


# Determine if player won or lost
if has_won:
    print(f"\nYou got it! The answer was {number_to_guess}")
else:
    print(f"\nYou've run out of guesses, you lose. The number was {number_to_guess}")