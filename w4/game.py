# ask the user to set the n (level), then randomly pick a number from 1 to n, then let the user guess the number.

import random


def main():
    lvl = level()  # get the level from the user
    x = random.randint(1, 10**lvl)  # get a random number from 1 to 10^n (level)

    while True:  # keep asking for guesses until the user is correct
        num = number()

        if num > x:
            print("Too large!")
        elif num < x:
            print("Too small!")
        else:
            print("Just right!")
            break  # exit the loop when the guess is correct


def level():
    while True:
        try:
            # ask the level. if it's not an int, reprompt until it is.
            lvl = int(input("Level: ").strip())

            if lvl < 1:
                continue

            return lvl

        except ValueError:
            continue


def number():
    while True:
        try:
            # ask a number. if it's not an int, reprompt until it is.
            num = int(input("Guess: ").strip())
            return num

        except ValueError:
            continue


if __name__ == "__main__":
    main()

# :( game.py outputs "Just right!" when guess is correct
#    timed out while waiting for program to exit
# solution: if __name__ == "__main__":
#               main()
