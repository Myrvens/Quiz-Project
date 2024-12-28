# A dictionary that stores questions and answers
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

# Have a variable that tracks the score of the player
score = 0

# Loop through the dictionary using the key-value pairs
for key, value in quiz.items():
    # Display each question to the user and allow them to answer
    print(value['question'])
    answer = input("Answer: ")
    
    # Tell them if they are right or wrong
    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1  # Increment the score if correct
        print("Your score is: " + str(score))
        print()  # Add spacing for readability
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print()  # Add spacing for readability

# Show the final result when the quiz is completed
print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")
