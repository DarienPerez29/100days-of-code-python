print('''
   ______                                   _       __             
  / ____/___ ____  _________ ______   _____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / ___/ / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /     / /__/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \___/_/ .___/_/ /_/\___/_/     
                                         /_/                       
\n''')

alphabet = "abcdefghijklmnopqrstuvwxyz"
run = True

def caesar(in_direction, in_text, in_shift):
    response = ""
    way = 1

    if in_direction == "decode": way = -1

    for c in in_text:
        if c in alphabet:
            new_pos = (alphabet.index(c) + (in_shift * way)) % len(alphabet)
            response += alphabet[new_pos]
    
    return f"Your {in_direction}d message is: {response}"

if __name__ == "__main__":

    while run:
        while True:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
            if direction == 'encode' or direction == 'decode': break
            else: print("\nPlease, enter a valid option...")

        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        print(caesar(in_direction = direction, in_text = text, in_shift = shift))
        decision = input("\nDo you want to run the program again? (yes/no): ").lower()
        print("\n")

        if decision == "no" or decision == "n":
            print("Goodbye!")
            run = False