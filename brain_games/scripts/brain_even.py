#!/usr/bin/env python3
from brain_games.games.even import get_even_task
from brain_games.user_interaction import run_game

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(TASK, get_even_task)


if __name__ == '__main__':
    main()
