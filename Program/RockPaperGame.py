import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    win_points = 0
    lose_points = 0

    while True:
        computer = random.choice(choices)

        user = input('Enter your choice (rock, paper, or scissors), or "q" to quit: ').lower()

        if user == 'q':
            break

        while user not in choices:
            user = input('Invalid choice. Please enter rock, paper, or scissors: ').lower()

        print(f'\nComputer chose: {computer}')
        print(f'You chose: {user}\n')

        if user == computer:
            print(f'Both players selected {user}. It\'s a tie!')
        elif user == 'rock':
            if computer == 'scissors':
                print('Rock smashes scissors! You win!')
                win_points += 1
            else:
                print('Paper covers rock! You lose.')
                lose_points += 1
        elif user == 'paper':
            if computer == 'rock':
                print('Paper covers rock! You win!')
                win_points += 1
            else:
                print('Scissors cuts paper! You lose.')
                lose_points += 1
        elif user == 'scissors':
            if computer == 'paper':
                print('Scissors cuts paper! You win!')
                win_points += 1
            else:
                print('Rock smashes scissors! You lose.')
                lose_points += 1

        print(f'Win points: {win_points}')
        print(f'Lose points: {lose_points}\n')

play_game()


