alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'encode' to encrypt, type 'decode ' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(in_text, in_shift):
    secret = ""

    for c in in_text:
        new_pos = (alphabet.index(c) + in_shift) % len(alphabet)
        secret += alphabet[new_pos]
    
    return secret

def decrypt(in_text, in_shift):
    result = ""

    for c in in_text:
        new_pos = (alphabet.index(c) - in_shift) % len(alphabet)
        result += alphabet[new_pos]
    
    return result

if __name__ == "__main__":
    if direction == "encode":
        print(encrypt(in_text = text, in_shift = shift))
    else:
        print(decrypt(in_text = text, in_shift = shift))
        