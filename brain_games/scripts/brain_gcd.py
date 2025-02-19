#!/usr/bin/env python3
from brain_games.games.gcd import get_gcd_task
from brain_games.user_interaction import run_game

TASK = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(TASK, get_gcd_task)


if __name__ == '__main__':
    main()
