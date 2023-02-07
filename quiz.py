
quiz = {
    "question1": {
        "question": "What is the capital of France",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland",
        "answer": "Zurich"
    },
    "question7": {
        "question": "What is the capital of Austria",
        "answer": "Vienna"
    },
    "question8": {
        "question": "What is the capital of Kenya",
        "answer": "Lusaka"
    }


}

score = 0
percentage = 0
while percentage < 85:
    for key, value in quiz.items():
        print(value['question'])
        answer = input("Answer? ")

        if answer.lower() == value['answer'].lower():
            print("correct")
            score += 1
            print(f"Your score is: {str(score)}")
            print("")

        else:
            print("Incorrect answer")
            print(f"The answer is: {value['answer']}")
            print(f"Your score is: {str(score)}")
            print("")

    percentage = int(score/8 * 100)
    print(f"You got {str(score)} out of 8 questions correctly")
    print(f"Your percentage is {str(percentage)}%")
    score = 0

    if percentage < 85:
        print("You need atleast 85% to pass")
        quits = input("Type Q to quit or enter to restart: ")

        if quits.lower() == "q":
            break