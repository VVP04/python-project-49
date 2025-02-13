from brain_games.games.prime import get_prime_task
from brain_games.user_interaction import run_game

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(TASK, get_prime_task)


if __name__ == '__main__':
    main()
