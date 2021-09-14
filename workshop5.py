import random


def guess_random_number(tries, start, stop):
    the_number = random.randint(start, stop)
    tries_orig = tries
    while tries > 0:
        print(
            f"\nGuess a number between {start} and {stop}. \nYou have {tries} guesses left.")
        try:
            guess = int(input("What is your guess? "))
        except:
            print("Play fair!!! That's not a number!!")
            continue
        tries -= 1
        if guess == the_number:
            print(
                f"\nYOU GUESSED IT!!! \nIt took you {tries_orig - tries} of your {tries_orig} guesses.")
            return
        else:
            print("Guess " + ("higher." if guess < the_number else "lower."))

    print(
        f"\nYOU FAILED!!!  It the number I was thinking of was {the_number}.")


def guess_random_num_linear(tries, start, stop):
    the_number = random.randint(start, stop)
    print("\nThe number for the progarm to guess is:", the_number)
    for guess in range(start, tries):
        print("Number of tries left:", tries)
        print("The program is guessing...", guess)
        if guess == the_number:
            print("The program has guessed the correct number!")
            return
        tries -= 1
    print("The program has failed to guess the correct number.")


def guess_random_num_binary(tries, start, stop):
    the_number = random.randint(start, stop)
    the_number = 71
    #the_number = 38
    print("\nRandom Number to find:", the_number)
    guess = start + (stop - start)//2
    verb = ""
    while tries > 0:
        print(tries, "Guessing"+verb+":", guess)

        if guess == the_number:
            print(f"Found it,{guess}!")
            return
        if guess > the_number:
            stop = guess
            verb = ",lower"
        else:
            start = guess
            verb = ",higher"

        guess = start + (stop - start)//2
        tries -= 1
    print("Your program has failed to guess the correct number.")


# driver task 1
"""
guess_random_number(5, 0, 10)
"""

# driver task 2
"""
guess_random_num_linear(5, 0, 10)
"""

# driver task 3
guess_random_num_binary(5, 0, 100)
