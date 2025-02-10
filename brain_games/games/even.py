import random


def check_for_parity(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    return 'no'


def get_even_task():
    random_number = random.randint(1, 100)
    return (random_number, check_for_parity(random_number))
