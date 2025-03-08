import random

def play_game():
    name = input("What is your name? ")
    print("Good Luck!", name)

    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)
    print("Guess the characters")

    guesses = ''
    turns = 12

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        print()  

        if failed == 0:
            print(f"{name}, You Win! 🎉")
            print("The word is:", word)
            break

        guess = input("Guess a character: ").lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong Guess ")
            print(f"You have {turns} more guesses.")

            if turns == 0:
                print(f"{name}, You Lose! ")
                print("The word was:", word)

    retry = input("Do you want to play again? (yes/no): ").lower()
    if retry == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
