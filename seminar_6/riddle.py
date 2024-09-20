"""Riddle Game"""

__all__ = ['riddle_game']

import random
from typing import Iterable


def riddle_func(riddle: str, possible_answers: list, correct_answer: str, num_of_tries: int) -> int:
    """Player is asked to guess a riddle within a number of tries from a
     given list of possible answers."""
    print(riddle)
    print(*possible_answers, sep='\n')
    num_of_tries_used = 0
    while num_of_tries:
        guess = input(f'Enter your guess to the riddle above:\t')
        if guess == correct_answer:
            print("You're right!")
            return num_of_tries_used + 1
        else:
            num_of_tries -= 1
            num_of_tries_used += 1
            print('Not quite right! ' + ('Try again' if num_of_tries !=0 else ''))

    print('You ran out of tries!')
    return 0


def riddle_game(num_of_tries: int=2) -> Iterable[int]:
    """Player is asked to guess a riddle within a number of tries from a
    given list of possible answers. Riddles are asked from a list."""
    riddles = [
        {
            "question": "Зимой и летом одним цветом. Что это?",
            "answers": ["Ель", "Сосна", "Берёза", "Клён"],
            "correct": "Ель"
        },
        {
            "question": "Висит груша, нельзя скушать. Что это?",
            "answers": ["Лампочка", "Яблоко", "Мандарин", "Персик"],
            "correct": "Лампочка"
        },
        {
            "question": "Без окон, без дверей, полна горница людей. Что это?",
            "answers": ["Огурец", "Картошка", "Арбуз", "Огурец"],
            "correct": "Огурец"
        },
        {
            "question": "Что можно видеть с закрытыми глазами?",
            "answers": ["Сон", "Картину", "Кино", "Фильм"],
            "correct": "Сон"
        }
    ]

    for item in riddles:
        num_of_tries_used = riddle_func(riddle=item['question'], possible_answers=item['answers'], correct_answer=item['correct'], num_of_tries=num_of_tries)
        yield item['question'], num_of_tries_used
    print('Game End')


_dict_results = {riddle:num_of_tries for riddle, num_of_tries in riddle_game()}


def print_result_func():
    """Prints results for each riddle guessed."""
    print('Results:')
    for riddle, num_of_tries in _dict_results.items():
        print(f'{riddle:<55}: {num_of_tries}')


if __name__ == '__main__':
    print_result_func()
