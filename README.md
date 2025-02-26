### Hexlet tests and linter status:
[![Actions Status](https://github.com/VVP04/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VVP04/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6cc4d2a77925785cdbb/maintainability.svg)](https://codeclimate.com/github/VVP04/python-project-49/maintainability)

---

### Table of contents

- [Description](#description)
- [Technologies](#technologies)
- [Installation](#installation)
- [Games](#games)
- [Development Workflow](#development-workflow)
- [Example Gameplay](#example-gameplay)

---

### Description

Brain games is a collection of 5 math-related games designed to challenge and improve your arithmetic skills. The games include:

- Checking if a number is prime
- Inserting a number into an arithmetic progression
- Providing the result of a calculation (multiplication, addition, subtraction)
- Answering if a number is even
- Finding the greatest common divisor of two numbers

---

### Technologies

- [Python ^3.12](https://www.python.org/)
- [Prompt ^0.4.1](https://pypi.org/project/prompt/)
- [Ruff ^0.9.5](https://astral.sh/ruff)

---

### Installation

#### Install uv:
```bash
pipx install uv
```
#### Install the package from the repository
```bash
uv pip install git+https://github.com/VVP04/python-project-49.git
```
#### Launch the game
```bash
make brain-games
```

---

### Games
#### To start playing, you can run the following commands:

#### To play "Check if a number is prime":
```bash
brain-prime
```
#### To insert a number into an arithmetic progression:
```bash
brain-progression
```
#### To provide the result of a calculation
```bash
brain-calc
```
#### To answer if a number is even:
```bash
brain-even
```
#### To find the greatest common divisor of two numbers:
```bash
brain-gcd
```

---

### Development Workflow
#### Install dependencies and configure the environment:
```bash
make install
```
#### Build a package:
```bash
make build
```
#### Install the build package locally:
```bash
make package-install
```
#### Launch the linter:
```bash
make lint
```

---

### Example Gameplay
#### brain-even: guess if a random number is even
[![asciicast](https://asciinema.org/a/704708.svg)](https://asciinema.org/a/704708)
#### brain-calc: calculate the result of a random expression 
[![asciicast](https://asciinema.org/a/704709.svg)](https://asciinema.org/a/704709)
#### brain-gcd: calculate the greatest common divisor for two random numbers
[![asciicast](https://asciinema.org/a/704710.svg)](https://asciinema.org/a/704710)
#### brain-progression: write down the missing element in arithemtic progression
[![asciicast](https://asciinema.org/a/5D7BnwJWcVlkIouvhCT3Kpb42.svg)](https://asciinema.org/a/5D7BnwJWcVlkIouvhCT3Kpb42)
#### brain-prime: guess if a random number is prime or not
[![asciicast](https://asciinema.org/a/uhL2FbNtwJYQzPoBnwFKW4jUt.svg)](https://asciinema.org/a/uhL2FbNtwJYQzPoBnwFKW4jUt)

---

### Project team

- [Владимир Плесовских](https://vk.com/id320156902) — Python developer