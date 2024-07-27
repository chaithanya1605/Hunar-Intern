def calculate_happiness():
    print("Answer the following questions with a number from 1-5, where 1 is 'Not at all' and 5 is 'Extremely'")

    questions = {
        "How happy are you with your life?": 0,
        "How often do you feel grateful?": 0,
        "How often do you exercise?": 0,
        "How happy are you with your relationships?": 0,
        "How often do you practice mindfulness?": 0
    }

    for question, answer in questions.items():
        while True:
            try:
                questions[question] = int(input(question + " "))
                if 1 <= questions[question] <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    happiness_score = sum(questions.values()) / len(questions)
    print(f"Your happiness score is {happiness_score:.2f} out of 5.")

    if happiness_score < 3:
        print("You may want to consider seeking help from a mental health professional.")
    elif happiness_score < 4:
        print("You're doing okay, but there's room for improvement.")
    else:
        print("You're doing great! Keep up the good work.")

calculate_happiness()
