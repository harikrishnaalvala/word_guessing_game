# Hangman Game

This is a simple **Hangman** game implemented in Python. The player must guess a randomly chosen word by entering one letter at a time. The game provides a limited number of attempts before the player loses.

## Features
✅ Randomly selects a word from a predefined list  
✅ Allows the player to guess letters one by one  
✅ Displays correct guesses and underscores for missing letters  
✅ Keeps track of the number of remaining guesses  
✅ Displays a **win** or **lose** message along with the correct word  
✅ Asks if the player wants to **retry** after the game ends  

## How to Play
1. Run the script in a Python environment.
2. Enter your name when prompted.
3. Start guessing letters to reveal the hidden word.
4. You have **12 attempts** to guess the word correctly.
5. If you guess all letters before running out of attempts, you **win**! 🎉
6. If you use all attempts without guessing the word, you **lose**. 😢
7. After the game ends, you can choose to **play again** or exit.

## Prerequisites
- Python 3.x installed on your system

## Running the Game
To run the game, use the following command in your terminal or command prompt:
```sh
python hangman.py
```

## Example Gameplay
```
What is your name? John
Good Luck! John
Guess the characters
_ _ _ _ _ _ _
Guess a character: p
Wrong Guess
You have 11 more guesses.
Guess a character: o
_ _ o _ _ _ _
...
John, You Win! 🎉
The word is: python
Do you want to play again? (yes/no):
```

## Contributing
Feel free to enhance this game by adding more words, improving the interface, or implementing additional features like difficulty levels!

## License
This project is free to use and modify for educational purposes.

