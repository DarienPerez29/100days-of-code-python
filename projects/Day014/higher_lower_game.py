import random
import modules.art as art
import modules.data as gd

# Function to print data in a formatted way
def print_formatted_option(data):
    print(f"""
\"{data['name'].upper()}\"
{data['description']}
has
{data['follower_count']},000,000 followers
""")

print(art.logo)

print('''
   ============================================
   >>> Who has more followers on Instagram? <<<
   ============================================
''')
input("         Press a key to continue...")

# Init variables with default values
option_a = random.choice(gd.data)
option_b = {}
score_a = 0
score_b = 0
final_score = 0

# Loop for playing until lose
has_lost = False
while not has_lost:
    option_b = random.choice(gd.data)
    score_a = option_a['follower_count']
    score_b = option_b['follower_count']

    print_formatted_option(option_a)
    print("====== vs =======")
    print_formatted_option(option_b)

    # Loop for requset for a valid response
    while True:
        print(f">> Does \"{option_b['name']}\" have higher ", end="")
        print(f"or lower followers than \"{option_a['name']}\"?")

        answer = input("   (Type higher or lower): ")

        if answer != "higher" and answer != "lower":
            print("\nPlease select a valid option...")
        else:
            break

    if (answer == "higher" and score_b >= score_a # Checks for higher
            or answer == "lower" and score_b <= score_a): # Checks for lower
        print("Correct")
        final_score += 1
        option_a = option_b
    else:
        print("You lose")
        has_lost = True

print(f"Your final score is: {final_score}")