import random


def gcd(num1: int, num2: int) -> int:
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2


def get_gcd_task():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    pair_for_gcd = f'{random_number1} {random_number2}'
    return (
        pair_for_gcd, 
        str(gcd(random_number1, random_number2))
        )
