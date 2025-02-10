import prompt


def run_game(task: str, game_func):
    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}")
    print(task)

    score = 0
    while score != 3:
        random_number, correct_answer = game_func()
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            break
    if score == 3:
        print(f"Congratulations, {username}!")
    else:
        print(
            f"{user_answer} is wrong answer ;(. "
            f"Correct answer was {correct_answer}."
        )
        print(f"Let's try again, {username}!")
