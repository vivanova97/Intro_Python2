"""
Guessing game.
"""

import random
from sys import argv


def guessing_game(lower_limit: int, upper_limit: int, num_of_tries: int) -> bool:
    """Guessing game in which the user enters a number within a given number of tries and is informed
    if the number is too high or too low."""

    rand_num = random.randint(lower_limit, upper_limit)

    while num_of_tries:
        guess = int(input(f'Enter your number between {lower_limit} - {upper_limit}:\t'))
        if guess == rand_num:
            print('You guessed it!')
            return True
        elif guess > rand_num:
            print('Too high!  The number is lower.')
            num_of_tries -= 1
        elif guess < rand_num:
            print('Too low!  The number is higher.')
            num_of_tries -= 1

    print('You ran out of tries!')
    return False


if __name__ =='__main__':
    LOWER_LIMIT, UPPER_LIMIT, NUM_OF_TRIES = list(map(int, argv[1:]))
    print(guessing_game(LOWER_LIMIT, UPPER_LIMIT, NUM_OF_TRIES))
    # help(guessing_game)
