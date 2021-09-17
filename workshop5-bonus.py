import random


def guess_random_number(tries, start, stop):
    the_number = random.randint(start, stop)
    tries_orig = tries
    old_guesses = set()
    while tries > 0:
        print(
            f"\nGuess a number between {start} and {stop}. \nYou have {tries} guesses left.")
        try:
            while True:
                guess = int(input("What is your guess? "))
                if guess in old_guesses:
                    print("You have already guessed that number! Try a different one.")
                    continue
                if (guess >= start and guess <= stop):
                    break
                print(
                    f"Guess out of range, please enter a number between {start} and {stop}.")
        except:
            print("That's not a valid number!!")
            continue
        tries -= 1
        old_guesses.add(guess)
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
            return True
        tries -= 1
    print("The program has failed to guess the correct number.")
    return False


def guess_random_num_binary(tries, start, stop):
    the_number = random.randint(start, stop)
    # the_number = 71
    # the_number = 38
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
"""
guess_random_num_binary(5, 0, 100)
"""
# bonus task 2


def choose_algo():
    tries = int(int_input("Number of attempts? "))
    start = int(int_input("Lowest Number? "))
    stop = int(int_input("Highest Number? "))
    while True:
        algo = input("[L]inear or [B]inary search? ").lower()
        if algo in ("l", "b", "linear", "binary"):
            break
    if algo in ("b",  "binary"):
        guess_random_num_binary(tries, start, stop)
    if algo in ("l",  "linear"):
        guess_random_num_linear(tries, start, stop)


def int_input(message):
    while True:
        try:
            val = int(input(message))
            return val
        except:
            print("Invalid input!!")

# bonus task 4


def gamble():
    bank = 10
    while 0 < bank < 50:
        while True:
            guess = input("Will the computer guess correctly, Y/N? ").lower()
            if guess == 'y' or guess == 'n':
                guess = True if guess == 'y' else False
                break
            print("Please answer Y/N")
        while True:
            max_bet = 10 if bank > 10 else bank
            try:
                bet = int(input("How much do you bet? $"))
                print("You are betting $"+str(bet))
                if 0 < bet <= max_bet:
                    break
                print("You must wager at least $1" if bet <
                      1 else "You can wager no more than $" + str(max_bet))
            except:
                print("Please enter a valid integer between 1 and", max_bet)
        if guess == guess_random_num_linear(12, 0, 20):
            print("\nYou win this round.")
            bank += bet
        else:
            print("\nYou lose this round.")
            bank -= bet
        print("Your current balance is $"+str(bank)+"\n")
    print("You Win!!!" if bank > 0 else "You Lose!!")


# bonus task2 driver
"""
choose_algo()
"""
# bonus task 3 driver
""""
guess_random_number(5, 0, 10)
"""

# bonus task 4 driver
gamble()
