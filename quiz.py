# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loops through the dicionary using the key value pairs
# display each question to the user and allow them to anser
# Tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1" : {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is thecapital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the cpaital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the cpaital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the cpaital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the cpaital of England?",
        "answer": "London"
    },
    "question7": {
        "question": "What is the cpaital of Netherlands?",
        "answer": "Amsterdam"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print(f"Your score is: {str(score)}")
    else: 
        print("Wrong!")
        print(f"The answer is: {value["answer"]}")

print(f"You got {score} out of 7 questions correctly")
print(f"Your percentage is {int(score/7 * 100)}%")