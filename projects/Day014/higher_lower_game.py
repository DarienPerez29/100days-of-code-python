import os
import random
import modules.art as art
import modules.data as gd

# Function to clear screen in windows or linux
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to print data of an option in a formatted way
def print_formatted_option(data, show_followers):
    print(f"\n\"{data['name'].upper()}\"")
    print(f"{data['description']}")

    if show_followers:
        print(f"has {data['follower_count']},000,000 followers")

    print()

# Function to print both options, a and b
def print_options(op_a, op_b):
    print_formatted_option(op_a, True)
    print("\t====== vs =======")
    print_formatted_option(op_b, False)

# Loop for replay game
playing = True
while playing:
    # Intro
    clear_screen()

    print(art.logo)

    print('''
    ============================================
    >>> Who has more followers on Instagram? <<<
    ============================================
    ''')
    input("         Press a key to continue...")

    clear_screen()

    # Init variables with default values
    option_a = random.choice(gd.data)
    option_b = {}
    score_a = 0
    score_b = 0
    score = 0

    # Loop for playing until lose
    has_lost = False
    while not has_lost:

        # Loop to select a different account
        while True:
            option_b = random.choice(gd.data)
            if option_b['name'] != option_a['name']:
                break
            
        score_a = option_a['follower_count']
        score_b = option_b['follower_count']

        # Loop for requset for a valid response (higher/lower)
        while True:
            print(art.logo)

            print(f"""
                ==================
                | Score: {score}\t|
                ==================""")


            print_options(option_a, option_b)

            print(f">> Does \"{option_b['name']}\" have higher ", end="")
            print(f"or lower followers than \"{option_a['name']}\"?")

            answer = input("   (Type higher or lower): ")

            if answer != "higher" and answer != "lower":
                clear_screen()
                print("\n>>>>>>>>>>>>>>>> Please select a valid option...")
            else:
                break

        # Check answer of player
        if (answer == "higher" and score_b >= score_a # Checks for higher
                or answer == "lower" and score_b <= score_a): # Checks for lower
            print("\n[CORRECT]: ", end = "")
            score += 1
            option_a = option_b
        else:
            print("\n[YOU LOSE]: ", end = "")
            has_lost = True
        print(f"{option_b['name']} has {option_b['follower_count']} million followers\n")
        
        input("Press a key to continue...")
        clear_screen()

    print(art.logo)

    print(f"""
    ========================================
            Your final score is: {score}  
    ========================================\n""")

    while True:
        option = input("Do you want to play again? (y/n)")

        if option == "n" or option == "no":
            clear_screen()
            print("Bye...")
            playing = False
            break
        elif option == "y" or option == "yes":
            break
        else:
            print("\nPlease select a valid option...")