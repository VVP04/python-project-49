from brain_games.consts import (
    MAX_PROGRESSION_LENGHT,
    MIN_PROGRESSION_LENGHT,
    PROGRESSION_INSTUCTION,
)
from brain_games.engine import run_game
from brain_games.utility import get_random_number


def get_progression_and_miss_num():
    start_progression = get_random_number()
    difference = get_random_number(0, 30)
    len_progression = get_random_number(MIN_PROGRESSION_LENGHT, 
                                        MAX_PROGRESSION_LENGHT)
    random_index = get_random_number(0, len_progression - 1)

    # Генерация прогрессии с пропущенным элементом
    progression = ' '.join([
        str(elem) if index != random_index else '..'
        for index, elem in enumerate(
            range(start_progression, 
                  start_progression + len_progression * difference, 
                  difference))
    ])

    # Получение пропущенного числа
    miss_num = str(start_progression + random_index * difference)

    return (progression, miss_num)


def run_progression_game():
    return run_game(PROGRESSION_INSTUCTION, get_progression_and_miss_num)
