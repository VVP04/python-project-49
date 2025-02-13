import random


def generate_progression(start: int, difference: int) -> list:
    progression = []
    while len(progression) != 10:
        progression.append(start)
        start = start + difference
    return progression


def get_progression_task():
    start = random.randint(1, 100)
    difference = random.randint(1, 30)
    progression = generate_progression(start, difference)
    random_index = random.randint(0, 9)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    return (' '.join([str(x) for x in progression]), correct_answer)
