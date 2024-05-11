# Libraries
import json
from time import sleep
import os
import operator
import math

# Json File
with open('calculator.json', 'r') as file:
    MESSAGES = json.load(file)

# Global Constants
VALID_OPERATIONS = ('add', 'sub', 'mul', 'truediv', 'pow',
                    'exp', 'log', 'sqrt', 'cbrt')

# Global dictionary of essential calculator values
calc_values = {
    "round_value": 2,
    "lang_value": "en"
}

# <============ DATA RETRIEVAL FUNCTIONS ============>
# Gets first or second number from user as float
def get_number(order):
    while True:
        number = input_prompt(get_current_lang(order))

        if invalid_number(number):
            print_prompt(get_current_lang('invalid_number'))
        else:
            return float(number)

# Returns valid operator from user for use with operator or math module
def get_operator():
    while True:
        operation = input_prompt(get_current_lang('operation'))

        if invalid_operator(operation):
            print_prompt(get_current_lang('invalid_operator'))
        else:
            return convert_operator(operation) # Module specific conversions

# Returns calculation rounded by user given value or default of 2
def get_calculation(operation, number1, number2):
    if isinstance(number2, float):
        operation = getattr(operator, operation) # operator.operation
        answer = operation(number1, number2)
    else:
        operation = getattr(math, operation) # math.operation
        answer = operation(number1)

    return str(round(answer, calc_values['round_value']))

# Gets the current rounding value
def get_current_rounding():
    return get_current_lang('current_round') + str(calc_values['round_value'])

# Retrieves current program language
def get_current_lang(msg):
    return MESSAGES[(calc_values['lang_value'])][msg]

# <============ MESSAGE FUNCTIONS ============>
# Prints out answer
#def print_answer(answer):
#    print_prompt(get_current_lang('answer') + answer + '\n')

def print_answer(number1, number2, operation, answer):
    reset_screen()

    valid_symbols = ('\u002B', '\u002D', '\u00D7', '\u00F7', '\u005E',
                     '\u0065\u005E', '\u33D2', '\u221A', '\u221B')
    symbols_dict = dict(zip(VALID_OPERATIONS, valid_symbols))
    symbol = symbols_dict[operation]

    print_prompt(get_current_lang('answer') + answer)

    if isinstance(number2, float):
        print_prompt(f'{number1} {symbol} {number2} = {answer}' + '\n')
    else:
        print_prompt(f'{symbol}{number1} = {answer}' + '\n')

# Returns input from a passed message in correct language
def input_prompt(message):
    if isinstance(message, list):
        message = format_message(message)
    return input(f'==> {message}' + '\n==> ').lower()

# Handles long messages from Json file and applys consistent formating
def format_message(message):
    return '\n==> '.join(message)

# Prints out message in correct language
def print_prompt(message):
    if isinstance(message, list):
        message = format_message(message)

    print(f'==> {message}')

# Welcome user for 3 seconds in chosen language
def welcome_user():
    print_prompt(get_current_lang('welcome'))
    sleep(3)

# Resets screen with support for Windows, Mac, and Linux
def reset_screen():
    if os.name == 'nt':
        os.system("cls") # Windows
    else:
        os.system("clear") # Mac/Linux

# <============ VALIDATION FUNCTIONS ============>
# Checks if program wants to take log of number less than 1
def invalid_unary_calculation(number1, operation):
    if operation == 'sqrt' and number1 < 0:
        return True
    elif operation == 'log' and number1 < 1:
        return True
    else:
        return False

# Checks if program wants to divide by 0
def zero_division(number2, operation):
    return number2 == 0 and operation == 'truediv'

# Checks if binary math operation
def binary_operation(operation):
    return operation in VALID_OPERATIONS[:5]

# Checks if user entered a valid number
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Checks if user entered a valid input ('1'-'9')
def invalid_operator(operation):
    return operation not in tuple(map(str, range(1,10)))

# Resets main program if user says yes in current language
def not_calculate_again():
    answer = input_prompt(get_current_lang('do_again'))
    return answer not in get_current_lang('yes')

# <============ DATA MANIPULATION FUNCTIONS ============>
# Handles pre-calculation config options
def config_options():
    while True:
        reset_screen()

        answer = input_prompt(get_current_lang('config'))

        if answer in (get_current_lang('valid_round')):
            change_rounding()
        elif answer in (get_current_lang('valid_lang')):
            change_lang()
        else:
            break

# Handles changing program session language
def change_lang():
    languages = ('en', 'es', 'fr')

    while True:
        answer = input_prompt(get_current_lang('change_lang'))

        if answer in languages:
            calc_values['lang_value'] = answer
            welcome_user()
            break

        print_prompt(get_current_lang('lang_error'))

# Handles changing program session rounding
def change_rounding():
    while True:
        print_prompt(get_current_rounding())
        answer = input_prompt((get_current_lang('change_rounding')))

        try:
            int(answer)
        except ValueError:
            print_prompt((get_current_lang('invalid_number')))
        else:
            if int(answer) in range(0, 21):
                calc_values['round_value'] = int(answer)
                break

            print_prompt(get_current_lang('round_error'))

# Converts operation input for use with get_attr()
def convert_operator(operation):
    op_dict = { num: VALID_OPERATIONS[num - 1] for num in range(1, 10) }
    return op_dict[int(operation)]

# <============ MAIN PROGRAM LOGIC ============>
# The actual calculator
def main_program():
    operation = get_operator()

    if binary_operation(operation): # Options 1-5
        number1, number2 = get_number('first'), get_number('second')
    else: # Options 6-9
        number1, number2 = get_number('single_value'), False

    while zero_division(number2, operation):
        print_prompt(get_current_lang('zero_error'))
        number2 = get_number('second')

    while invalid_unary_calculation(number1, operation): # logs/sqrts
        print_prompt(get_current_lang('unary_calculation_error'))
        number1 = get_number('single_value')

    answer = get_calculation(operation, number1, number2)
    print_answer(number1, number2, operation, answer)

# Starts program
def start():
    welcome_user()
    config_options() # For answer rounding and languages

    while True:
        reset_screen()
        main_program()
        if not_calculate_again():
            break

    print_prompt(get_current_lang('bye'))

# Begin program
start()
