def find_runner_up(scores):
    # Check if the input list has at least 2 scores
    if len(scores) < 2:
        return "Not enough scores to determine a runner-up"

    # Remove duplicates by converting the list to a set
    unique_scores = set(scores)

    # Check if there's a runner-up score
    if len(unique_scores) < 2:
        return "No runner-up score (all scores are the same)"

    # Find the runner-up score
    runner_up_score = sorted(unique_scores)[-2]

    return runner_up_score

# Get the scores from the user
scores = input("Enter the scores separated by spaces (max 100 scores, 0-100): ")

# Convert the input string to a list of integers
scores = [int(score) for score in scores.split()]

# Check if the input list has more than 100 scores
if len(scores) > 100:
    print("Too many scores (max 100 allowed)")
else:
    # Find and print the runner-up score
    print(find_runner_up(scores))

