import json
import random


def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)


def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        choice = int(input("Enter option number: "))
        selected = q["options"][choice - 1]

        if selected == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Answer:", q["answer"])

    return score


def save_result(score, total):
    result = {"score": score, "total": total}

    with open("result.json", "w") as f:
        json.dump(result, f, indent=4)


# MAIN
questions = load_questions()
random.shuffle(questions)

score = run_quiz(questions)

print(f"\n Final Score: {score}/{len(questions)}")

save_result(score, len(questions))
print("Result saved!")
