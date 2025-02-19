#!/usr/bin/env python3
from brain_games.games.progression import get_progression_task
from brain_games.user_interaction import run_game

TASK = 'What number is missing in the progression?'


def main():
    run_game(TASK, get_progression_task)


if __name__ == '__main__':
    main()
