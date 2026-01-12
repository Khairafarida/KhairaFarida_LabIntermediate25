secret_word = "cat"
guessed_letters = set()

while True:
    letter = input("Masukkan satu huruf: ")

    if len(letter) == 1 and letter.isalpha():
        if letter.lower() in secret_word.lower():
            guessed_letters.add(letter.lower())
            print("Huruf tersebut ADA di dalam kata rahasia.")
        else:
            print("Huruf tersebut TIDAK ADA di dalam kata rahasia.")
    else:
        print("Input tidak valid! Masukkan tepat satu huruf saja.")

    if set(secret_word) == guessed_letters:
        print("\nSemua huruf berhasil ditebak!")
        print("Kata rahasia adalah:", secret_word)
        break