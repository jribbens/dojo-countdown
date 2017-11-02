#!/usr/bin/env python3

import random
from human import human
from solve import solve

LARGE = (25, 50, 75, 100)
SMALL = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10)
TARGET = (101, 1000)
CARDS = 6


def computer(numbers, target):
    computer = solve.solve_numbers(numbers, target, False)
    if isinstance(computer, str):
        return computer, target
    return computer[0], computer[1]


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
    numbers, target = interface()
    print("Target is: {}   Your cards are: {}".format(
        target, ", ".join(str(number) for number in numbers)))
    human_solution = human(numbers, target)
    computer_solution, computer_result = computer(numbers, target)
    human_result = eval(human_solution)
    print("Humamn has: {}: {}\nComputer has: {}: {}\n".format(
        human_solution, human_result, computer_solution, computer_result))
    human_diff = abs(human_result - target)
    computer_diff = abs(computer_result - target)
    if human_diff < computer_diff:
        print("Human wins!")
    elif computer_diff < human_diff:
        print("Computer wins!")
    else:
        print("It's a draw!")
