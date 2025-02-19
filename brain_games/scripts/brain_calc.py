#!/usr/bin/env python3
from brain_games.games.calc import get_calc_task
from brain_games.user_interaction import run_game

TASK = 'What is the result of the expression?'


def main():
    run_game(TASK, get_calc_task)


if __name__ == '__main__':
    main()
