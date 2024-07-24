import time

questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the smallest country in the world?": "Vatican City",
    "Who wrote Romeo and Juliet?": "William Shakespeare"
}

def quiz_game():
    print("Welcome to the quiz game!")
    print("You have 60 seconds to answer the questions.")
    print("Good luck!\n")

    start_time = time.time()
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answer}.\n")

        if time.time() - start_time > 60:
            print("Time's up!")
            break

    print(f"Your final score is {score} out of {len(questions)}.")

quiz_game()
