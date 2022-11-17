import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Queen, King and Jack have a value of 10

def get_deck_str(deck, hide):
    if hide: 
        return str(deck[0]) + ", ■"
    return ', '.join(map(str, deck))

def get_deck_sum(deck, hide):
    if hide:
        return deck[0]
    return sum(deck)

player_cards = []
computer_cards = []

for i in range(2):
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

print("=================================================")
print(f"Your cards: {get_deck_str(player_cards, False)} \t|| Total: {get_deck_sum(player_cards, False)}")
print("-------------------------------------------------")
print(f"Computer cards: {get_deck_str(computer_cards, True)} \t|| Total: {get_deck_sum(computer_cards, True)}")
print("=================================================")