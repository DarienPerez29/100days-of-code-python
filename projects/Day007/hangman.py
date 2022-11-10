import modules.art as art
import modules.words as words

chosen_word = words.getRandomWord()
lives = art.getHangmanArtLen() - 1
logo = art.getLogo()
guessed_letters = []

# Set display
display = []
for c in chosen_word: display.append("_")

# Starting game
print(logo)

on_game = True
while on_game:
    guess = input("\nGuess a letter: ").lower()
    print("\n")
    
    if guess in guessed_letters:
        print("You've already tried that letter, try another\n")
    else:
        # Change display if letter guessed is found
        for i, c in enumerate(chosen_word):
            if c == guess: display[i] = c
        
        # lose a live if guess wrong
        if guess not in chosen_word: 
            print(f"Letter '{guess}' is not in the word to guess")
            lives -= 1

        print(" ".join(display))
        print("\n" + art.getHangmanArt(lives))

        if "_" not in display:
            on_game = False
            print("\n=== YOU WIN !!! ===")
        elif lives == 0:
            on_game = False
            print("\nYou lose :c")
            print(f"The word was: {chosen_word}")

    guessed_letters.append(guess)