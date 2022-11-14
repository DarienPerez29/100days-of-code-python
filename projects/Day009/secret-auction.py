import os
import art

bidders_dictionary = {}
register_bidder = True
max_bid = 0
max_bideer = ""
draw = False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

print(art.logo)
print("Welcome to the secret auction program.\n")

while register_bidder:
    input_name = input("What is your name?: ").capitalize()
    input_bid = int(input("What's your bid?: $"))
    print("\n")

    bidders_dictionary[input_name] = input_bid

    while True:
        extra_bidder = input("Are there any other bidders? (yes/no)").lower()
        if extra_bidder == "no" or extra_bidder == "n":
            register_bidder = False
            break
        elif extra_bidder == "yes" or extra_bidder == "y":
            break
        else:
            clear_screen()
            print("Select a valid option...")

    clear_screen()


for bidder in bidders_dictionary:
    current_bid = bidders_dictionary[bidder]
    if current_bid > max_bid:
        max_bid = current_bid
        max_bidder = bidder
        draw = False
    elif current_bid == max_bid:
        draw = True

if not draw:
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
else:
    print("There's a draw...")