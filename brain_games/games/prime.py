import math
import random


def is_prime(num: int) -> str:
    for divisor in range(2, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            return 'no'
    return 'yes'


def get_prime_task():
    random_number = random.randint(1, 100)
    return (random_number, is_prime(random_number))
