# Libraries
import json
import os
import operator
import math

# Json File
with open('calculator.json', 'r') as file:
    data = json.load(file)

# Resets main program if user says yes in current language
def calculate_again():
    answer = input_prompt(current_lang('do_again'))
    return answer in current_lang('yes')

# Prints out answer
def print_answer(answer):
    print_prompt(current_lang('answer') + answer)

# Returns calculation rounded by user given value or default of 2
def get_calculation(operation, number1, number2):
    if isinstance(number2, float):
        operation = getattr(operator, operation) # operator.operation
        answer = operation(number1, number2)
    else:
        operation = getattr(math, operation) # math.operation
        answer = operation(number1)

    return str(round(answer, data['round_value']))

# Checks if program wants to divide by 0
def zero_division(number2, operation):
    return number2 == 0 and operation == 'truediv'

# Checks if binary math operation
def binary_operation(operation):
    return operation in data['operators']['binary']

# Checks if user entered a valid number
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# Gets first or second number from user as float
def get_number(order):
    while True:
        number = input_prompt(current_lang(order))

        if invalid_number(number):
            print_prompt(current_lang('invalid_number'))
        else:
            return float(number)

# Checks if user entered a valid input (1-9)
def invalid_operator(operation):
    return operation not in data['operators']['valid']

# Gets valid operator from user for use with operator or math module
def get_operator():
    while True:
        operation = input_prompt(current_lang('operation'))

        if invalid_operator(operation):
            print_prompt(current_lang('invalid_operator'))
        else:
            return data['operators'][operation] # Module specific conversions

# Gets all values needed for a calculation
def get_values():
    operation = get_operator()
    number1 = get_number('first')
    if binary_operation(operation):
        number2 = get_number('second')
    else:
        number2 = False

    return (operation, number1, number2)

# The actual calculator
def main_program():
    operation, number1, number2 = get_values()

    while zero_division(number2, operation):
        print_prompt(current_lang('zero_error'))
        number2 = get_number('second')

    answer = get_calculation(operation, number1, number2)
    print_answer(answer)

# Handles changing program session language
def change_lang():
    while True:
        answer = input_prompt(current_lang('change_lang'))

        if answer in data['languages']:
            data['lang_value'] = answer
            break

        print_prompt(current_lang('lang_error'))

# Gets the current rounding value
def current_round():
    return current_lang('current_round') + str(data['round_value'])

# Handles changing program session rounding
def change_rounding():
    while True:
        print_prompt(current_round())
        answer = input_prompt((current_lang('change_rounding')))

        try:
            int(answer)
        except ValueError:
            print_prompt((current_lang('invalid_number')))
        else:
            data['round_value'] = abs(int(answer))
            break

# Handles pre-calculation config options
def config_options():
    while True:
        reset_screen()

        answer = input_prompt(current_lang('config'))

        if answer in (current_lang('valid_round')):
            change_rounding()
        elif answer in (current_lang('valid_lang')):
            change_lang()
        else:
            break

# Returns input from a passed message in correct language
def input_prompt(message):
    message = format_message(message)
    return input(f'==> {message}').lower()

# Handles long messages from Json file and applys consistent formating
def format_message(message):
    if isinstance(message, list):
        return '\n==> '.join(message) + '\n==> '
    return message + '\n==> '

# Prints out message in correct language
def print_prompt(message):
    message = format_message(message)
    print(f'==> {message}')

# Retrieves current program language
def current_lang(msg):
    return data[(data['lang_value'])][msg]

# Resets screen with support for Windows, Mac, and Linux
def reset_screen():
    if os.name == 'nt':
        os.system("cls") # Windows
    else:
        os.system("clear") # Mac/Linux

# Starts program
def start():
    print_prompt(current_lang('welcome'))
    config_options()

    while True:
        reset_screen()
        main_program()
        if not calculate_again():
            break

    print_prompt(current_lang('bye'))

# Begin program
start()
