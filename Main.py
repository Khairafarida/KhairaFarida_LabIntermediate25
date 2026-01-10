
secret_word = "cat"

letter = input("Masukkan satu huruf: ")

if len(letter) == 1 and letter.isalpha():

    if letter.lower() in secret_word.lower():
        print("Huruf tersebut ADA di dalam kata rahasia.")
    else:
        print("Huruf tersebut TIDAK ADA di dalam kata rahasia.")
else:
    print("Input tidak valid! Masukkan tepat satu huruf saja.")