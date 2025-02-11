import random


def calculate(num1: int, num2: int, operation: str) -> int:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def get_calc_task():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    random_operator = random.choice(['+', '-', '*'])
    numeric_expression = f'{random_number1} {random_operator} {random_number2}'
    return (numeric_expression, str(calculate(random_number1, random_number2, random_operator)))
