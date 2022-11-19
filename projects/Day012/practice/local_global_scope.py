# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

## Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength) # Doesnt' work

## Global scope
player_health = 10
player_magic = 5

def drink_potion():
    potion_strength = 2
    global player_magic
    player_magic += 2
    print(potion_strength)

drink_potion()
print(player_health, player_magic)