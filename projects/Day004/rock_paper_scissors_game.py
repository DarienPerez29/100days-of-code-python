import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
# Rock, paper, scissors by Veronica Karlsson
# from https://www.asciiart.eu/people/body-parts/hand-gestures

hands = [rock, paper, scissors]

print('''
===========================================
||| WELCOME TO ROCK PAPER SCISSORS GAME |||
===========================================\n''')

print("What do you choose? (Type the number of the option):")
print("[1] Rock")
print("[2] Paper")
print("[3] Scissors")

player_move = int(input()) - 1
pc_move = random.randint(0, 2)

print("\n\n-------------------------------------------")
print("Your move:")
print(hands[player_move])
print("\n---\n")
print("Computer's move:")
print(hands[pc_move])
print("\n-------------------------------------------")

print("\n\n================= RESULTS =================\n")

if player_move == pc_move:
    print("\t\tDRAW")
else:
    if player_move == 0: # Player moves: rock
        if pc_move == 1: # PC moves: paper
            print("\t\tYOU LOSE :C")
        else: # PC moves: scissors
            print("\t\tYOU WIN :D !!!")
    elif player_move == 1: # Player moves: paper
        if pc_move == 2: # PC moves: paper
            print("\t\tYOU LOSE :C")
        else: # PC moves: scissors
            print("\t\tYOU WIN :D !!!")
    elif player_move == 2: # Player moves: scissors
        if pc_move == 0: # PC moves: paper
            print("\t\tYOU LOSE :C")
        else: # PC moves: scissors
            print("\t\tYOU WIN :D !!!")

print("\n===========================================")





