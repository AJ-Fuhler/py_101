import random
import os

VALID_CHOICES = [
    'rock', 'paper', 'scissors', 'lizard', 'spock', 'r', 'p', 'sc', 'l', 'sp']

def prompt(message):
    print(f"==> {message}")

def update_score():
    global player_score, computer_score
    if ((choice == 'rock' and computer_choice in ['scissors', 'lizard']) or
        (choice == 'paper' and computer_choice in ['rock', 'spock']) or
        (choice == 'scissors' and computer_choice in ['paper', 'lizard']) or
        (choice == 'lizard' and computer_choice in ['paper', 'spock']) or
        (choice == 'spock' and computer_choice in ['scissors', 'rock'])):
        player_score += 1
        prompt('You win this round!')
    elif ((choice == 'rock' and computer_choice in ['paper', 'spock']) or
        (choice == 'paper' and computer_choice in ['scissors', 'lizard']) or
        (choice == 'scissors' and computer_choice in ['rock', 'spock']) or
        (choice == 'lizard' and computer_choice in ['rock', 'scissors']) or
        (choice == 'spock' and computer_choice in ['lizard', 'paper'])):
        computer_score += 1
        prompt('Computer wins this round!')
    else:
        prompt("You tied this round!")


def display_winner():
    if player_score == 3:
        prompt('You are the GRAND WINNER!')
    else:
        prompt('Computer is the GRAND WINNER!')
        prompt('Better luck next time...')

def get_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES[:5])}')
    player_choice = input().lower()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input().lower()

    if player_choice in VALID_CHOICES[5:]:
        player_choice = convert_shortened_choice(player_choice)

    return player_choice

def convert_shortened_choice(user_input):
    match user_input:
        case 'r':
            user_input = 'rock'
        case 'p':
            user_input = 'paper'
        case 'sc':
            user_input = 'scissors'
        case 'l':
            user_input = 'lizard'
        case 'sp':
            user_input = 'spock'

    return user_input


def display_game_rules():
    prompt(
    '''Game Rules:

    Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons
    Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats
    paper, paper disproves Spock, Spock vaporizes rock, and rock crushes
    scissors. Whoever throws the winning signal wins! If both of you make the
    same signal, it's a tie.

    This is a Best of Five. Whoever reaches 3 wins first, wins the match!
    ''')

def play_again():
    prompt('Do you want to play again (y/n)?')
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    return answer

def display_score(pl_score, pc_score):
    prompt(f'You {pl_score} | {pc_score} Computer')

def reset_score():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

player_score = 0
computer_score = 0

while True:
    os.system('clear')
    display_game_rules()
    display_score(player_score, computer_score)
    choice = get_choice()
    computer_choice = random.choice(VALID_CHOICES[:5])
    prompt(f'You chose {choice}, computer chose {computer_choice}')
    update_score()
    if player_score >= 3 or computer_score >= 3:
        display_winner()
        reset_score()
        play_again_answer = play_again()
        if play_again_answer[0] == 'n':
            break