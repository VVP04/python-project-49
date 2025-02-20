from brain_games.consts import GCD_INSTUCTION
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def gcd(num1: int, num2: int) -> int:
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2


def get_numbers_and_gcd() -> tuple:
    num1, num2 = get_random_number(), get_random_number()
    gcd_pair = f"{num1} {num2}"
    return (gcd_pair, str(gcd(num1, num2)))


def run_gcd_game():
    return run_game(GCD_INSTUCTION, get_numbers_and_gcd)
