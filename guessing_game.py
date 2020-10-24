"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys  # imports sys used to exit the system when player quits

highscore = [100]  # list highscore set to 100 the max number of guesses


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    # Welcome message
    print("\n-------------------------------------------------------------")
    print("==========   Welcome to the Number Guessing Game  ===========")
    print("-------------------------------------------------------------\n")

    # displays current high score
    print("\t\tThe Current High Score is: {}\n".format(highscore[-1]))

    number = random.randint(1, 100)  # creates a random number between 1 and 100
    attempts = 0  # variable attempts to store number of attempts

    while True:

        # try except to catch any errors
        try:
            guess = int(input("Guess a number between 1-100 >>> "))
            if guess <= 0:
                print("Only guess numbers between from 1 and 100, \nPlease Try Again...")
            elif guess > 100:
                print("Sorry! Please guess a number between 1 and 100... \nPlease Try Again...")
        except ValueError:
            print("You need to enter only numbers to guess...")
        else:
            if guess == number:
                attempts += 1
                if attempts < highscore[-1]:
                    print(
                        "You guessed right the number was {} it took you {} try(s) that is a new record".format(number,
                                                                                                                attempts))
                    if attempts < highscore[-1]:
                        highscore.append(attempts)
                else:
                    print("You guessed right the number was {} it took you {} try(s)".format(number, attempts))
                break
            elif guess < number:
                attempts += 1
                print("your Guess is to LOW")  # lets user know guess is to low
                continue
            elif guess > number:
                attempts += 1
                print("Your guess is to HIGH")  # lets user know guess is to high

    # ask the user if they want to play again
    play_again = input("Would you like to play again? [y]es or [n]o: ")
    if play_again.lower()[0] == 'y':
        start_game()
    else:
        print("Thanks for playing!")
        sys.exit


# Kick off the program by calling the start_game function.
start_game()
