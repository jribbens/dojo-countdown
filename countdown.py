#!/usr/bin/env python3

import random
from solve import solve

LARGE = (25, 50, 75, 100)
SMALL = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10)
TARGET = (101, 1000)
CARDS = 6

def solve_countdown(numbers, target):
    return solve.solve_numbers(numbers, target)


def choose(values, quantity):
    values = list(values)
    return [
        values.pop(random.randrange(len(values)))
        for _ in range(quantity)
    ]


def interface():
    num_large = int(input("How many large cards? (0-{}) ".format(len(LARGE))))
    if not 0 <= num_large <= len(LARGE):
        raise ValueError("You must choose between 0 and {} large cards.".format(
            len(LARGE)))
    numbers = choose(LARGE, num_large) + choose(SMALL, CARDS - num_large)
    target = random.randrange(TARGET[0], TARGET[1])
    return numbers, target


if __name__ == "__main__":
    print(interface())
