from brain_games.consts import EVEN_INSTUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_num_and_even_check() -> tuple:
    num = get_random_number()
    result = 'yes' if is_even(num) else 'no'
    return (num, result)


def run_even_game():
    return run_game(EVEN_INSTUCTION, get_num_and_even_check)
