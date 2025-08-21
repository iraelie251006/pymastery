questions = {
    1: {
        "question": "What is Python?",
        "options": ["a programming language", "a snake", "a type of food"],
        "answer": "a programming language"
    },
    2: {
        "question": "Which data type is used to store multiple items in Python?",
        "options": ["string", "integer", "list"],
        "answer": "list"
    },
    3: {
        "question": "What symbol is used for comments in Python?",
        "options": ["//", "#", "/*"],
        "answer": "#"
    },
    4: {
        "question": "Which function is used to get user input in Python?",
        "options": ["input()", "get()", "read()"],
        "answer": "input()"
    },
    5: {
        "question": "What does 'len()' function do in Python?",
        "options": ["calculates length of an object", "creates a new list", "converts to lowercase"],
        "answer": "calculates length of an object"
    }
}


def take_quiz(questions):
    score = 0
    total_questions = len(questions)

    print("Quiz started!")
    print(f"There are {total_questions} questions in the quiz")

    for q_num, q_data in questions.items():
        print(f"Question {q_num}: {q_data["question"]}")

        for i, option in enumerate(q_data["options"], 1):
            print(f"    {i}. {option}")

        while True:
            try:
                options_len = len(q_data["options"])
                choice = input(f"Enter your answer (1-{options_len}): ")
                choice = int(choice)

                if choice >= 1 and choice <= options_len:
                    break
                else:
                    print("Please enter a number within range")
            except:
                print("Please enter a valid number")

        user_answer = q_data["options"][choice - 1]

        if user_answer == q_data["answer"]:
            print("Hurray, You nailed it flawlessly")
            score += 1
        else:
            print("Incorret answer.")

        print("===========================")

    return (score, total_questions)


def display_results(score, total):
    percentage = (score / total) * 100

    print("")
    print("------- Quiz -------")
    print("")

    print(f"Your percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent")
    elif percentage >= 50:
        print("Good Job")
    else:
        print("You need to improve")


def main():
    print(" welcome to the python Quiz App")
    score, total_questions = take_quiz(questions)
    display_results(score, total_questions)

    while True:
        play_again = input("Do you wish to play again (yes / no): ").lower()

        if play_again == "no":
            break
        score, total_questions = take_quiz(questions)
        display_results(score, total_questions)


main()
