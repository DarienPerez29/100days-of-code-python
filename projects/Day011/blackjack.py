import os
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Queen, King and Jack have a value of 10

# Function to clear screen in windows or linux
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to return list values in string
def get_deck_str(deck, hide):
    if hide: 
        return str(deck[0]) + ", ■"
    return ', '.join(map(str, deck))

# Function to return sum of list values
def get_deck_sum(deck, hide):
    if hide:
        return deck[0]
    return sum(deck)

# Function to print scoreborad
def print_scoreboard(is_player_turn):
    print(art.logo, "\n\n")
    print("|---------------- SCOREBOARD -------------------|")
    print("=================================================")
    print(f"| Your cards: {get_deck_str(player_cards, False)} \t|| Total: {player_score}")
    print("-------------------------------------------------")
    print(f"| Computer cards: {get_deck_str(computer_cards, is_player_turn)} \t|| Total: {computer_score}")
    print("=================================================\n")

# Variables
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0

player_turn = True
winner = ""

# initial decks
for i in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
computer_score = get_deck_sum(computer_cards, player_turn) # Set computer score to display to the player

clear_screen()

# =====================================
# Loop for the player to get more cards
# =====================================
while player_turn:
    # The score of the desks is asked
    player_score = get_deck_sum(player_cards, False)
    
    # If player score is perfect (21), they doesn't need to get more cards
    if player_score == 21:
        player_turn = False
        break
    # If player score is greater than 21, they automatically loses
    elif player_score > 21:
        winner = "computer"
        player_turn = False
        break

    print_scoreboard(player_turn)

    # If an invalid option is passed, the program asks again
    while True:
        action = str(input("Do you want to get another card? (y/n): ")).lower()
        clear_screen()

        if action == "y" or action == "yes":
            player_cards.append(random.choice(cards))
            break
        elif action == "n" or action == "no":
            player_turn = False
            break
        else:
            clear_screen()
            print_scoreboard(player_turn)
            print("Please, select a valid option...")
# ===================================== player's turn ends

computer_score = get_deck_sum(computer_cards, player_turn) # Get real computer's score

# If computer already won, the game is over
if winner == "computer":
    # End of game 1
    print_scoreboard(player_turn)
    print("\t       You went over...")
    print(art.loser_icon)
else:    
    # Loop for computer turn
    while computer_score < player_score and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = get_deck_sum(computer_cards, False)

    # End of game 2
    print_scoreboard(player_turn)
    
    if computer_score > 21:
        print("\t    Opponent went over.")
        print(art.winner_icon)
    elif player_score > computer_score:
        print(art.winner_icon)
    elif player_score < computer_score:
        print(art.loser_icon)
    elif player_score == computer_score:
        print("Draw!")
        