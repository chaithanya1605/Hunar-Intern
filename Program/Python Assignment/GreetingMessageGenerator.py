def generate_greeting(first_name, last_name):
    greeting_message = f"Hello, {first_name} {last_name}! Nice to meet you."
    return greeting_message

# Get the user's first and last names
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# Generate and print the greeting message
print(generate_greeting(first_name, last_name))


