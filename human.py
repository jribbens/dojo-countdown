import re


def verify_attempt(attempt, numbers):
    numbers = list(numbers)
    for match in re.findall(r"[0-9]+", attempt):
        number = int(match)
        try:
            numbers.pop(numbers.index(number))
        except ValueError:
            return "The unavailable number {} was used.".format(number)
    try:
        return eval(attempt)
    except ValueError:
        return "The attempt could not be understood."


def human(numbers, target):
    solution = None
    while True:
        attempt = input("Enter your attempt: {}".format(
            "(or 'done') " if solution else "")).strip()
        if solution and attempt == "done":
            return solution
        result = verify_attempt(attempt, numbers)
        if isinstance(result, int):
            solution = attempt
            if result == target:
                print("Exact hit!")
                return solution
            print("You have {}: {} away.".format(result, abs(target - result)))
        else:
            print(result)
