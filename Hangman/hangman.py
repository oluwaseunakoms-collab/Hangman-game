import random

words = ["python", "hangman", "keyboard", "monitor", "science"]
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

while incorrect_guesses < max_incorrect:
    
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if "_" not in display:
        print("You won! The word was:", secret_word)
        break

    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        incorrect_guesses += 1
        print(f"Wrong! '{guess}' is not in the word.")
    else:
        print(f"Good guess! '{guess}' is not in the word.")
else:
    print(f"Game over! The word was: {secret_word}")