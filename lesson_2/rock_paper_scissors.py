import random
import os
import time

VALID_CHOICES = [
    'rock', 'paper', 'scissors', 'lizard', 'spock', 'r', 'p', 's', 'l', 'sp']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f"==> {message}")


def display_winner(end_score):
    print()
    prompt("And that's three!\n")
    time.sleep(1)
    if end_score['p_wins'] == 3:
        prompt('You are the GRAND WINNER!\n')
        time.sleep(1)
    else:
        prompt('Computer is the GRAND WINNER!\n')
        time.sleep(1)
        prompt('Better luck next time...\n')
        time.sleep(1)

def get_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES[:5])}')
    player_choice = input().lower()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input().lower()

    if player_choice in VALID_CHOICES[5:]:
        player_choice = convert_shortened_choice(player_choice)

    return player_choice

def convert_shortened_choice(player_choice):
    match player_choice:
        case 'r':
            player_choice = 'rock'
        case 'p':
            player_choice = 'paper'
        case 's':
            player_choice = 'scissors'
        case 'l':
            player_choice = 'lizard'
        case 'sp':
            player_choice = 'spock'

    return player_choice


def display_game_rules():
    prompt(
    '''Game Rules:

    Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons
    Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats
    paper, paper disproves Spock, Spock vaporizes rock, and rock crushes
    scissors. Whoever throws the winning signal wins! If both of you make the
    same signal, it's a tie.

    Tip: if you're feeling lazy, you can type: 
    'r' for rock
    'p' for paper
    's' for scissors 
    'l' for lizard
    'sp' for spock

    This is a Best of Five. Whoever reaches 3 wins first, wins the match!
    ''')

def display_welcome_prompt():
    prompt('Welcome to Rock Paper Scissors Lizard Spock!\n')

def play_again():
    prompt('Do you want to play again (y/n)?')
    answer = input().lower()

    while True:
        if answer in ['y', 'n']:
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    return answer

def display_score(player_score, pc_score):
    prompt(f'You {player_score} | {pc_score} Computer')

def reset_score(score_dict):
    for outcome in score_dict:
        score_dict[outcome] = 0

def display_round_winner(player_choice, pc_choice):
    if pc_choice in WINNING_COMBOS[[player_choice]]:
        prompt('You win this round!')
    elif player_choice in WINNING_COMBOS[pc_choice]:
        prompt('You win this round!')
    else:
        prompt('You tied this round!')

def update_score(player_choice, pc_choice, current_score):
    if pc_choice in WINNING_COMBOS[player_choice]:
        current_score['p_wins'] += 1
    elif player_choice in WINNING_COMBOS[pc_choice]:
        current_score['c_wins'] += 1
    else:
        current_score['ties'] += 1
    time.sleep(2)

def display_choices(player_choice, pc_choice):
    prompt(f'You chose {player_choice}, computer chose {pc_choice}\n')
    time.sleep(1)


def main():
    score = { #MAKE THIS WORK INSTEAD OF USING global player_score etc..
        "p_wins": 0,
        "c_wins": 0,
        "ties": 0,
    }

    while True:
        os.system('clear')
        display_welcome_prompt()
        display_game_rules()
        display_score(score['p_wins'], score['c_wins'])
        choice = get_choice()
        computer_choice = random.choice(VALID_CHOICES[:5])
        display_choices(choice, computer_choice)
        display_round_winner(choice, computer_choice)
        update_score(choice, computer_choice, score)

        if score['p_wins'] >= 3 or score['c_wins'] >= 3:
            display_winner(score)
            play_again_answer = play_again()
            if play_again_answer[0] == 'y':
                reset_score(score)
            else:
                break

main()