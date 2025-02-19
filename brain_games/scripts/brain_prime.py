#!/usr/bin/env python3
from brain_games.consts import PRIME_INSTUCTION
from brain_games.engine import run_game
from brain_games.games.prime import get_prime_task


def main():
    run_game(PRIME_INSTUCTION, get_prime_task)


if __name__ == '__main__':
    main()
