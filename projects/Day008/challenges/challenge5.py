alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(in_direction, in_text, in_shift):
    response = ""
    way = 1

    if in_direction == "decode": way = -1

    for c in in_text:
        new_pos = (alphabet.index(c) + (in_shift * way)) % len(alphabet)
        response += alphabet[new_pos]
    
    return response

if __name__ == "__main__":
    print(caesar(in_direction = direction, in_text = text, in_shift = shift))
        