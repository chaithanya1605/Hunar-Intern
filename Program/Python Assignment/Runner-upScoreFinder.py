def find_runner_up(scores):
    # Remove duplicates by converting the list to a set
    unique_scores = set(scores)

    # Check if there's a runner-up score
    if len(unique_scores) < 2:
        return "No runner-up score"

    # Find the runner-up score
    runner_up_score = sorted(unique_scores)[-2]

    return runner_up_score


# Get the scores from the user
scores = input("Enter the scores separated by spaces: ")

# Convert the input string to a list of integers
scores = [int(score) for score in scores.split()]

# Find and print the runner-up score
print(find_runner_up(scores))

