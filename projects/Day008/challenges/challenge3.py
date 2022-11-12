alphabet = "abcdefghijklmnopqrstuvwxyz"

direction = input("Type 'enconde' to encrypt, type 'decode ' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(enc_text, enc_shift):
    secret = ""

    for c in enc_text:
        new_pos = (alphabet.index(c) + enc_shift) % len(alphabet)
        secret += alphabet[new_pos]
    
    return secret

if __name__ == "__main__":
    print(encrypt(enc_text = text, enc_shift = shift))