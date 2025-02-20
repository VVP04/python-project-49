from brain_games.consts import PRIME_INSTUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5 + 1)):
        if num % divisor == 0:
            return False
    return True


def get_num_and_prime_check() -> tuple:
    num = get_random_number()
    return (num, 'yes' if is_prime(num) else 'no')


def run_prime_game():
    return run_game(PRIME_INSTUCTION, get_num_and_prime_check)
