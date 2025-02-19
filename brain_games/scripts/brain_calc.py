#!/usr/bin/env python3
from brain_games.consts import CALC_INSTUCTION
from brain_games.engine import run_game
from brain_games.games.calc import get_calc_task


def main():
    run_game(CALC_INSTUCTION, get_calc_task)


if __name__ == '__main__':
    main()
