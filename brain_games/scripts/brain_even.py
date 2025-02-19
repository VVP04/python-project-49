#!/usr/bin/env python3
from brain_games.consts import EVEN_INSTUCTION
from brain_games.engine import run_game
from brain_games.games.even import get_even_task


def main():
    run_game(EVEN_INSTUCTION, get_even_task)


if __name__ == '__main__':
    main()
