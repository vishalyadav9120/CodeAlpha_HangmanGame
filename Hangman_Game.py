import random

# List of words
words = ["apple", "mango", "grapes", "tiger", "chair"]

# Random word choose karna
word = random.choice(words)

# Guessed letters store karne ke liye
guessed_letters = []

# Wrong guesses count
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print(f"You have {max_wrong_guesses} wrong guesses allowed.\n")

# Game loop
while wrong_guesses < max_wrong_guesses:
    # Current word display banana
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Agar word complete ho gaya
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.\n")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    # Add guess
    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print("✅ Correct guess!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! Remaining chances: {max_wrong_guesses - wrong_guesses}\n")

# If user loses
if wrong_guesses == max_wrong_guesses:
    print("💀 Game Over! You ran out of guesses.")
    print("The word was:", word)