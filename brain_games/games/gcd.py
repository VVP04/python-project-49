from math import gcd

from brain_games.consts import GCD_INSTUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def get_numbers_and_gcd() -> tuple:
    num1, num2 = get_random_number(start=1), get_random_number(start=1)
    gcd_pair = f"{num1} {num2}"
    result_of_gcd = gcd(num1, num2)
    return (gcd_pair, str(result_of_gcd))


def run_gcd_game():
    return run_game(GCD_INSTUCTION, get_numbers_and_gcd)
