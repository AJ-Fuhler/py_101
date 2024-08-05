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

VALID_CHOICES = CHOICE_ABBREVIATIONS.items()

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

def get_choice():
    prompt(f'Choose one: {", ".join(CHOICE_ABBREVIATIONS)}')
    player_choice = input().lower()

    while player_choice not in VALID_CHOICES: # FIX THIS CODE, VALID_CHOICES is a list of tuples.
        prompt("That's not a valid choice")
        player_choice = input().lower()

    # if player_choice in VALID_CHOICES:
     #   player_choice = convert_shortened_choice(player_choice)

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

def display_choices(player_choice, pc_choice):
    prompt(f'You chose {player_choice}, computer chose {pc_choice}\n')
    time.sleep(1)

def determine_round_winner(player_choice, pc_choice):
    if pc_choice in WINNING_COMBOS[player_choice]:
<<<<<<< HEAD
        return 'p_wins'
    elif player_choice in WINNING_COMBOS[pc_choice]:
        return 'c_wins'
    else:
        return 'ties'

def display_round_winner(player_choice, pc_choice):
    outcome = determine_round_winner(player_choice, pc_choice)
    if outcome == 'p_wins':
        prompt('You win this round!')
    elif outcome == 'c_wins':
        prompt('Computer wins this round!')
=======
        prompt('You won this round!')
    elif player_choice in WINNING_COMBOS[pc_choice]:
        prompt('Computer won this round!')
>>>>>>> 4016e23 (ensured final score is displayed in rps. also worked on practice problems)
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

def play_again():
    prompt('Do you want to play again (y/n)?')
    answer = input().lower()

    while True:
        if answer in ['y', 'n']:
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    return answer

def reset_score(score_dict):
    for outcome in score_dict:
        score_dict[outcome] = 0

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
        computer_choice = random.choice(CHOICE_ABBREVIATIONS)
        display_choices(choice, computer_choice)
        display_round_winner(choice, computer_choice)
        update_score(choice, computer_choice, score)

        if score['p_wins'] >= 3 or score['c_wins'] >= 3:
            os.system('clear')
            display_welcome_prompt()
            display_game_rules()
            display_score(score['p_wins'], score['c_wins'])
            display_winner(score)
            play_again_answer = play_again()
            if play_again_answer[0] == 'y':
                reset_score(score)
            else:
                break

main()