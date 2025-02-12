import random


def generate_progression(start_of_progression: int, difference_of_progression: int) -> list:
    progression = []
    while len(progression) != 10:
        progression.append(start_of_progression)
        start_of_progression = start_of_progression + difference_of_progression
    return progression


def get_progression_task():
    start = random.randint(1,100)
    difference = random.randint(1,30)
    progression = generate_progression(start, difference)
    random_index = random.randint(0,9)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    return (' '.join([str(x) for x in progression]), correct_answer)
