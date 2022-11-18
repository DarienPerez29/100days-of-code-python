import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Queen, King and Jack have a value of 10

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

# Variables
player_cards = []
computer_cards = []
player_score = 0
computer_score = 0

hit = True
winner = ""

# initial decks
for i in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
computer_score = get_deck_sum(computer_cards, True) # Set computer score to display to the player

# Loop so the player can get more cards
while hit:
    # The score of the desks is asked
    player_score = get_deck_sum(player_cards, False)

    print("=================================================")
    print(f"Your cards: {get_deck_str(player_cards, False)} \t|| Total: {player_score}")
    print("-------------------------------------------------")
    print(f"Computer cards: {get_deck_str(computer_cards, True)} \t|| Total: {computer_score}")
    print("=================================================\n")

    # If player score is perfect (21), they doesn't need to get more cards
    if player_score == 21:
        break
    # If player score is greater than 21, they automatically loses
    elif player_score > 21:
        winner = "computer"
        break

    # If an invalid option is passed, the program asks again
    while True:
        action = str(input("Do you want to get another card? (y/n): ")).lower()

        if action == "y" or action == "yes":
            player_cards.append(random.choice(cards))
            break
        elif action == "n" or action == "no":
            hit = False
            break
        else:
            print("\nPlease, select a valid option...")

if winner == "computer":
    print("You went over, you lose :C")
else:
    computer_score = get_deck_sum(computer_cards, False)

    while computer_score < player_score:
        computer_cards.append(random.choice(cards))
        computer_score = get_deck_sum(computer_cards, False)

    print("=================================================")
    print(f"Your cards: {get_deck_str(player_cards, False)} \t|| Total: {player_score}")
    print("-------------------------------------------------")
    print(f"Computer cards: {get_deck_str(computer_cards, False)} \t|| Total: {computer_score}")
    print("=================================================\n")
    
    if computer_score > 21:
        print("Opponent went over. You win :D")
    elif player_score > computer_score:
        print("You win :D")
    elif player_score < computer_score:
        print("You lose :c")
    elif player_score == computer_score:
        print("Draw!")
        