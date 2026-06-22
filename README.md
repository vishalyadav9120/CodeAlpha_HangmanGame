# Hangman Game

## Project Details
- **Project Name:** Hangman Game
- **Domain:** Python Programming
- **Language Used:** Python 3
- **Internship:** CodeAlpha Python Programming Internship
- **Developer:** Vishal Yadav

---

## Objective
To develop a simple text-based Hangman game where the player guesses a hidden word one letter at a time.  
The player is allowed a maximum of **6 wrong guesses** to complete the word.

---

## Description
This is a **console-based Hangman Game** built using **Python**.  
The program randomly selects a word from a predefined list and asks the user to guess the word **one letter at a time**.

- If the guessed letter is correct, it is revealed in the word.
- If the guessed letter is wrong, the number of wrong guesses increases.
- The game continues until the player guesses the complete word or reaches the maximum number of wrong guesses.

This project is useful for understanding basic Python concepts such as:
- loops
- conditionals
- strings
- lists
- user input handling

---

## Features
- Random word selection from a predefined list
- Maximum **6 wrong guesses**
- Single-letter input validation
- Tracks guessed letters
- Displays the current word using underscores
- Win and lose messages
- Beginner-friendly console game

---

## Concepts Used
- **Random Module**
- **Variables**
- **Lists**
- **Strings**
- **While Loop**
- **If-Else Statements**
- **User Input / Output**
- **Input Validation**

---

## Algorithm
1. Import the `random` module.
2. Create a list of predefined words.
3. Select one random word from the list.
4. Create an empty list for guessed letters.
5. Set `wrong_guesses = 0`.
6. Set `max_wrong_guesses = 6`.
7. Display the hidden word using underscores.
8. Ask the user to enter one letter.
9. Check whether the entered value is a valid single alphabet letter.
10. If the letter has already been guessed, show a message.
11. If the guessed letter is in the word, reveal it in the displayed word.
12. If the guessed letter is not in the word, increase `wrong_guesses` by 1.
13. Continue the loop until:
    - the player guesses the whole word, or
    - the player uses all 6 wrong guesses.
14. Display the final result (Win / Lose).

---

## Input
The user enters **one letter at a time** from the keyboard.

### Example Input
```text
a
h
n
g
m.
---
Output
Example Output
Welcome to Hangman Game!
Guess the word one letter at a time.
You have 6 wrong guesses allowed.

Word: _ _ _ _ _ _ _

Enter a letter: a
Good job! 'a' is in the word.

Word: _ a _ _ _ a _

Enter a letter: h
Good job! 'h' is in the word.

...

Congratulations! You guessed the word.

If the player is unable to guess the word in 6 wrong attempts, the game shows a Game Over message and displays the correct word.

File Structure
CodeAlpha_HangmanGame/
│── Hangman_Game.py
│── README.md
How to Run
Make sure Python 3 is installed on your system.
Download or clone this repository.
Open the project folder in terminal or VS Code.
Run the following command:
python Hangman_Game.py
Sample Program Flow
The game starts with a welcome message.
A random word is selected.
The player enters one letter at a time.
Correct letters are revealed in the word.
Wrong letters increase the wrong guess count.
The game ends with either:
Congratulations! You guessed the word, or
Game Over! Better luck next time.
Conclusion

The Hangman Game demonstrates the use of Python fundamentals such as loops, conditions, strings, lists, and the random module.
It is a simple yet interactive project for beginners and helps in understanding how to build a small command-line game in Python.

Author

Vishal Yadav


---
