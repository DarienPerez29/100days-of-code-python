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

# Loop for playing until lose
has_lost = False
while not has_lost:
    option_b = random.choice(gd.data)

    print_formatted_option(option_a)
    print("\tvs")
    print_formatted_option(option_b)

    break