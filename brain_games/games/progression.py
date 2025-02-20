from brain_games.consts import (
    MAX_PROGRESSION_LENGHT,
    MIN_PROGRESSION_LENGHT,
    PROGRESSION_INSTUCTION,
)
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def generate_progression() -> list:
    progression = []
    start_progression = get_random_number()
    difference = get_random_number(0, 30)
    len_progression = get_random_number(MIN_PROGRESSION_LENGHT, 
                                        MAX_PROGRESSION_LENGHT)
    for _ in range(len_progression):
        progression.append(start_progression)
        start_progression = start_progression + difference
    return (progression, len_progression)


def get_progression_and_miss_num():
    progression, len_progression = generate_progression()
    random_index = get_random_number(0, len_progression - 1)
    miss_num = progression[random_index]
    progression[random_index] = '..'
    return (' '.join([str(x) for x in progression]), str(miss_num))


def run_progression_game():
    return run_game(PROGRESSION_INSTUCTION, get_progression_and_miss_num)
