word = "cat"
attempts = 6
guessed = []

print("HANGMAN 2.0")
print("You have 6 attempts")

while attempts > 0:
    print("\nAttempts left:", attempts)

    # show the word 
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    guess = input("\nGuess a letter: ")

    # check input validity
    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)
    attempts -= 1

    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")

    # check win condition
    if all(letter in guessed for letter in word):
        print("\nYou WIN! The word is:", word)
        break

if attempts == 0:
    print("\nGame Over! The word was:", word)