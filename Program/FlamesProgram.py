def flames_game(name1, name2):
    # Remove common letters
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)

    # Count remaining letters
    count = len(name1) + len(name2)

    # Determine the relationship
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    index = (count - 1) % 6
    relationship = flames[index]

    # Print the result
    print(f"The relationship between {name1} and {name2} is {relationship}.")

    # Explain the relationship
    if relationship == 'F':
        print("Friendship")
    elif relationship == 'L':
        print("Love")
    elif relationship == 'A':
        print("Affection")
    elif relationship == 'M':
        print("Marriage")
    elif relationship == 'E':
        print("Enemy")
    elif relationship == 'S':
        print("Sibling")

# Get names from user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Play the game
flames_game(name1, name2)
