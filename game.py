import copy
import json
import random
import time

possible_answers = {0: 'a.', 1: 'b.', 2: 'c.', 3: 'd.'}


def change_highscore():
    pass


def run_game(player: dict, questions_path: str = "questions.json") -> int:
    score = 0

    with open(questions_path, "r") as f:
        questions = json.loads(f.read())
        questions = questions['questions']

    copy_questions = copy.deepcopy(questions)

    while copy_questions:
        questions_object = random.choice(copy_questions)

        print(questions_object)
        print(questions_object['question'])

        for index, answer in enumerate(questions_object['answers']):
            print(f"\t{possible_answers[index]} {answer}")

        pick = input("Alege raspunsul corect: ")
        answers = {v: k for k, v in possible_answers.items()}
        if answers[f"{pick}."] == questions_object['correctIndex']:
            print("Correct answer.")
            score += 1
        else:
            print("Wrong answer.")

        copy_questions.remove(questions_object)

    print(f"You have answer to {score} questions corectly.")
    if score > list(player.keys())[0]['high_score']:
        change_highscore()

    return 1
