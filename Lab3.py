def updateText(secret_word, guessed_letters):
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else: 
            display += "_ "

    return display

def hangman():
    secret_word = "cat"
    guessed_letters = []
    lives = 5

    print("Let's play the game!")

    while lives > 0:
        print("\nWord:", updateText(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Oops, you already picked that one!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Ding ding ding! Nice guess!")
        else:
            lives -= 1
            print("Wrong guess, Try again!")
            print("Remaining chances:", lives)

        if "_" not in updateText(secret_word, guessed_letters):
            print("\nYay you cracked the word! The word is:", secret_word)
            return

    print("\nOh no, better luck next time!")
    print("The secret word was:", secret_word)

hangman()