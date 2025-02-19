#!/usr/bin/env python3
from brain_games.consts import GCD_INSTUCTION
from brain_games.engine import run_game
from brain_games.games.gcd import get_gcd_task


def main():
    run_game(GCD_INSTUCTION, get_gcd_task)


if __name__ == '__main__':
    main()
