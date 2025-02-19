import prompt

from brain_games.consts import NUMBER_OF_ROUNDS


def run_game(instruction: str, get_question_and_answer):
    username = prompt.string(
        "Welcome to the Brain Games!\n"
        "May I have your name? "
        )
    
    print(
        f"Hello, {username}!\n"
        f"{instruction}"
        )

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(
            f"Question: {question}\n"
            f"Your answer: "
            )
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
            f"{user_answer} is wrong answer ;(. "
            f"Correct answer was {correct_answer}.\n"
            f"Let's try again, {username}!"
            )
            return
    print(f'Congratulations, {username}!')
