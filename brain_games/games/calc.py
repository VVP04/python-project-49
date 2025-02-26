from random import choice

from brain_games.consts import CALC_INSTUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def get_operations():
    return [
        ('+', lambda x, y: x + y),
        ('-', lambda x, y: x - y),
        ('*', lambda x, y: x * y)
    ]


def get_numeric_expression_and_result() -> tuple:
    num1, num2 = get_random_number(), get_random_number()
    math_operator, operation = choice(get_operations())
    numeric_expression = f'{num1} {math_operator} {num2}'
    result = operation(num1, num2)
    return (numeric_expression, str(result))


def run_calc_game():
    return run_game(CALC_INSTUCTION, get_numeric_expression_and_result)
