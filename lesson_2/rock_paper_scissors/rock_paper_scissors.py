# Libraries
import json
import os
import sys
from random import choice

# Json File
with open('rps.json', 'r') as file:
    MESSAGES = json.load(file)

# Global Constants
MOVES = ('scissors', 'spock', 'lizard', 'rock', 'paper')
HELP = ('h', 'H', 'help', 'HELP')
QUIT = ('q!', 'Q!', 'quit!', 'QUIT!')
SHORT_MOVES = ('s', 'sp', 'l', 'r', 'p')
WINNING_CONDITIONS = {
    'scissors': ('lizard', 'paper'),
    'spock': ('scissors', 'rock'),
    'lizard': ('paper', 'spock'),
    'rock': ('scissors', 'lizard'),
    'paper': ('rock', 'spock')
}

# <============ MESSAGE FUNCTIONS ============>
def print_prompt(message):
    print(f'==> {message}')

def input_prompt(message):
    if isinstance(message, list):
        message = format_message(message)

    return input(f'==> {message}' + '\n==> ').lower()

def show_welcome_screen(user_name, comp_name):
    print_prompt(f"{MESSAGES['welcome']} {user_name}!\U0001F60A")
    print_prompt(f"{MESSAGES['opponent']} {comp_name}!\U0001F4AA")
    input_prompt(MESSAGES['rules'])
    reset_screen()

def show_score_board(game_data):
    rounds = fetch_rounds(game_data)
    target = fetch_target(game_data)
    user_name, comp_name = fetch_names(game_data)
    user_wins, comp_wins = fetch_wins(game_data)
    name_wins = f'{user_name}: {user_wins} | {comp_name}: {comp_wins}'

    print('+' + f' Round: {rounds} '.center(len(name_wins), '-') + '+')
    print('|' + (' ' * len(name_wins)) + '|')
    print(f'|{name_wins}|')
    print('|' + (' ' * len(name_wins)) + '|')
    print('+' + f' Best of: {target} '.center(len(name_wins), '-') + '+')

def show_game_help(game_data):
    input_prompt(MESSAGES['rules'])
    reset_screen()
    show_score_board(game_data)

def show_invalid_move(game_data):
    reset_screen()
    show_score_board(game_data)
    print_prompt(MESSAGES['invalid_move'])

def show_round_winner(game_data):
    show_moves(game_data)
    user_name, comp_name = fetch_names(game_data)
    winner = game_data['winner']

    if winner == user_name:
        print_prompt(f'{user_name} wins!')
    elif winner == comp_name:
        print_prompt(f'{comp_name} wins!')
    else:
        print_prompt(MESSAGES['draw'])

def show_moves(game_data):
    user_name, comp_name = fetch_names(game_data)
    user_move, comp_move = fetch_moves(game_data)

    print_prompt(f'{user_name} chose {user_move}')
    print_prompt(f'{comp_name} chose {comp_move}')

def show_wins(game_data):
    user_wins, comp_wins = fetch_wins(game_data)
    print_prompt(f'Player has {user_wins}. Computer has {comp_wins}')

def show_game_winner(winner):
    print_prompt(f'The winner is: {winner}!\U0001f600')

# <============ DATA RETRIEVAL FUNCTIONS ============>
def get_user_name():
    while True:
        name = input_prompt(MESSAGES['name'])

        if valid_user_name(name):
            name = capitalize_name(name)
            return name

        reset_screen()
        print_prompt(MESSAGES['invalid_name'])

def get_comp_name():
    return choice(('Monty', 'Guido', 'Linus'))

def get_win_target():
    while True:
        target = input_prompt(MESSAGES['target'])

        if valid_target(target):
            reset_screen()
            return int(target)

        reset_screen()
        print_prompt(MESSAGES['invalid_target'])

def get_user_move(game_data):
    while True:
        move = input_prompt(MESSAGES['move'])

        if move in MOVES:
            return move
        if move in SHORT_MOVES:
            return convert_move(move)

        if move in HELP:
            show_game_help(game_data)
        elif move in QUIT:
            quit_game()
        else:
            show_invalid_move(game_data)

def get_comp_move():
    return choice(MOVES)

def play_again():
    while True:
        answer = input_prompt(MESSAGES['play_again'])

        match answer:
            case ('y' | 'yes'):
                return True
            case ('n' | 'no'):
                return False
            case _:
                print_prompt(MESSAGES['invalid_play_again'])

# <============ OBJECT CONSTRUCTOR FUNCTIONS ============>
def construct_game_data(user_name, comp_name, win_target):
    return {
      user_name: { 'wins': 0, 'move': None },
      comp_name: { 'wins': 0, 'move': None },
      'target': win_target,
      'rounds': 1,
      'winner': None,
    }

# <============ DATA MANIPULATION FUNCTIONS ============>
# Splits long json messages into seperate lines
def format_message(message):
    return '\n==> '.join(message)

# In case user enters more than first name
def capitalize_name(name):
    name = name.split(' ')
    name = [ names.capitalize() for names in name ]
    return ' '.join(name)

# In case user enters short-hand move
def convert_move(move):
    move_dict = dict(zip(SHORT_MOVES, MOVES))
    return move_dict[move]

# Mutates game_data!
def update_scoreboard(game_data):
    user_name, comp_name = fetch_names(game_data)

    if user_won(game_data):
        game_data[user_name]['wins'] += 1
    elif comp_won(game_data):
        game_data[comp_name]['wins'] += 1

    game_data['rounds'] += 1

# <============ FETCH FUNCTIONS ============>
def fetch_names(game_data):
    return tuple(game_data.keys())[:2]

def fetch_target(game_data):
    return game_data['target']

def fetch_rounds(game_data):
    return game_data['rounds']

def fetch_wins(game_data):
    user_name, comp_name = fetch_names(game_data)

    user_wins = game_data[user_name]['wins']
    comp_wins = game_data[comp_name]['wins']

    return (user_wins, comp_wins)

def fetch_moves(game_data):
    user_name, comp_name = fetch_names(game_data)

    user_move = game_data[user_name]['move']
    comp_move = game_data[comp_name]['move']

    return (user_move, comp_move)

# <============ PREDICATE FUNCTIONS ============>
def valid_user_name(name):
    name = name.replace(' ', '')
    return len(name) in range(2, 50) and name.isalpha()

def valid_target(target):
    try:
        target = int(target)
    except ValueError:
        return False

    if target not in range(1, 11):
        return False

    return True

def user_won(game_data):
    user_name, _ = fetch_names(game_data)
    return game_data['winner'] == user_name

def comp_won(game_data):
    _, comp_name = fetch_names(game_data)
    return game_data['winner'] == comp_name

def no_winner(game_data):
    user_wins, comp_wins = fetch_wins(game_data)
    target = fetch_target(game_data)
    return target > user_wins and target > comp_wins

def someone_won(game_data):
    user_wins, comp_wins = fetch_wins(game_data)
    target = fetch_target(game_data)
    return user_wins >= target or comp_wins >= target

# <============ CALCULATION FUNCTIONS ============>
def calculate_winner(game_data):
    user_name, comp_name = fetch_names(game_data)
    user_move, comp_move = fetch_moves(game_data)

    if comp_move in WINNING_CONDITIONS[user_move]:
        return user_name
    if user_move in WINNING_CONDITIONS[comp_move]:
        return comp_name
    return None

# <============ TERMINAL FUNCTIONS ============>
def reset_screen():
    if os.name == 'nt':
        os.system("cls") # Windows
    else:
        os.system("clear") # Mac/Linux

def quit_game():
    print_prompt(MESSAGES['goodbye'])
    sys.exit(0)

# <============ MAIN PROGRAM LOGIC ============>
def play():
    user_name = get_user_name()
    comp_name = get_comp_name()
    win_target = get_win_target()
    game_data = construct_game_data(user_name, comp_name, win_target)
    show_welcome_screen(user_name, comp_name)
    show_score_board(game_data)

    while True:
        game_data[user_name]['move'] = get_user_move(game_data)
        game_data[comp_name]['move'] = get_comp_move()
        game_data['winner'] = calculate_winner(game_data)
        update_scoreboard(game_data)

        reset_screen()
        show_score_board(game_data)
        show_round_winner(game_data)

        if someone_won(game_data):
            show_game_winner(game_data['winner'])

            if not play_again():
                print_prompt(MESSAGES['goodbye'])
                break

            game_data = construct_game_data(user_name, comp_name, win_target)
            reset_screen()
            show_score_board(game_data)
play()
