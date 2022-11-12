alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'enconde' to encrypt, type 'decode ' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(text, shift):
    secret = ""

    for c in text:
        secret += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    
    return secret

if __name__ == "__main__":
    print(encrypt(text = text, shift = shift))