import random
import os
import time

CHOICE_ABBREVIATIONS = {
    'rock': ['r'],
    'paper': ['p'],
    'scissors': ['s', 'sc'],
    'lizard': ['l'],
    'spock': ['sp'],
}

VALID_CHOICES =  [
    item for key, value in CHOICE_ABBREVIATIONS.items()
         for item in [key] + value]

COMPUTER_CHOICES = list(CHOICE_ABBREVIATIONS.keys())

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f"==> {message}")

def display_welcome_prompt():
    prompt('Welcome to Rock Paper Scissors Lizard Spock!\n')

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

def display_score(player_score, pc_score):
    prompt(f'You {player_score} | {pc_score} Computer')

def get_full_choice(abbreviation):
    for key, values in CHOICE_ABBREVIATIONS.items():
        if abbreviation in values:
            return key
    return abbreviation

def get_choice():
    prompt(f'Choose one: {", ".join(CHOICE_ABBREVIATIONS)}')
    player_choice = input().strip().lower()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input().strip().lower()

    return get_full_choice(player_choice)

def display_choices(player_choice, pc_choice):
    prompt(f'You chose {player_choice}, computer chose {pc_choice}\n')
    time.sleep(1)

def determine_round_winner(player_choice, pc_choice):
    if pc_choice in WINNING_COMBOS[player_choice]:
        return 'p_wins'
    if player_choice in WINNING_COMBOS[pc_choice]:
        return 'c_wins'

    return 'ties'

def display_round_winner(player_choice, pc_choice):
    outcome = determine_round_winner(player_choice, pc_choice)
    if outcome == 'p_wins':
        prompt('You win this round!')
    elif outcome == 'c_wins':
        prompt('Computer wins this round!')
    else:
        prompt('You tied this round!')

def update_score(player_choice, pc_choice, current_score):
    outcome = determine_round_winner(player_choice, pc_choice)
    current_score[outcome] += 1
    time.sleep(2)

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

def ask_play_again():
    prompt('Do you want to play again (y/n)?')
    answer = input().strip().lower()

    while True:
        if answer in ['y', 'n']:
            break

        prompt('Please enter "y" or "n".')
        answer = input().strip().lower()

    if answer == 'y':
        return True

    return False

def reset_score(score_dict):
    for outcome in score_dict:
        score_dict[outcome] = 0

def match_winner(score_dict):
    if score_dict['p_wins'] >= 3 or score_dict['c_wins'] >= 3:
        return True
    return False

def main():
    score = {
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
        computer_choice = random.choice(COMPUTER_CHOICES)
        display_choices(choice, computer_choice)
        display_round_winner(choice, computer_choice)
        update_score(choice, computer_choice, score)

        if match_winner(score):
            os.system('clear')
            display_welcome_prompt()
            display_game_rules()
            display_score(score['p_wins'], score['c_wins'])
            display_winner(score)
            play_again_answer = ask_play_again()
            if play_again_answer:
                reset_score(score)
            else:
                break

main()