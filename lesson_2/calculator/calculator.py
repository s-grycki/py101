# zero_division should now be handled when getting the second number

# Libraries
import pdb
import json
import os
import operator
import math

# Json File
with open('calculator.json', 'r') as file:
    data = json.load(file)

# Function Declarations
def print_prompt(message):
    message = format_message(message)
    print(f'==> {message}')

def input_prompt(message):
    message = format_message(message)
    return input(f'==> {message}').lower()

def format_message(message):
    if type(message) is list:
        return '\n==> '.join(message) + '\n==> '
    else:
        return message + '\n==> '

def reset_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def get_number(order):
    while True:
        number = input_prompt(current_lang(order))

        if invalid_number(number):
            print_prompt(current_lang('invalid_number'))
        else:
            return float(number)

def get_operator():
    while True:
        operation = input_prompt(current_lang('operation'))

        if invalid_operator(operation):
            print_prompt(current_lang('invalid_operator'))
        else:
            return operation

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def invalid_operator(operation):
    return operation not in data['operators']['valid']

def calculation(operation, number1, number2):
    if operation == '4' and number2 == 0: # Handles dividing by 0
        print_prompt(current_lang('zero_error'))
    elif number2:
        operation = getattr(operator, data['operators'][operation])
        print_prompt((current_lang('answer') +
        calculate_answer(operation, number1, number2)))
    else:
        operation = getattr(math, data['operators'][operation])
        print_prompt((current_lang('answer') +
        calculate_answer(operation, number1)))

def calculate_answer(operation, number1, number2 = False):
    if number2:
        answer = operation(number1, number2)
        return str(round(answer, data['round_value']))
    else:
        answer = operation(number1)
        return str(round(answer, data['round_value']))

def calculate_again():
    answer = input_prompt(current_lang('do_again'))
    return True if answer in current_lang('yes') else False

def play():
    while True:
        reset_screen()
        print_prompt(current_lang('welcome'))
        answer = input_prompt(current_lang('config'))

        if answer in (current_lang('valid_round')):
            change_rounding()
        elif answer in (current_lang('valid_lang')):
            change_lang()
        else:
            break

    main_loop()

def change_rounding():
    while True:
        answer = input_prompt((current_lang('change_rounding')))

        try:
            int(answer)
        except ValueError:
            print_prompt((current_lang('invalid_number')))
        else:
            data['round_value'] = abs(int(answer))
            break

def current_round(msg):
    return data[(data['round_value'])][msg]

def change_lang():
    while True:
        answer = input_prompt(current_lang('change_lang'))

        if answer in data['languages']:
            data['lang_value'] = answer
            break
        else:
            print_prompt(current_lang('lang_error'))

def current_lang(msg):
    return data[(data['lang_value'])][msg]

def main_loop():
    while True:
        operation = get_operator()
        number1 = get_number('first')

        if operation in data['operators']['valid'][:5]:
            number2 = get_number('second')
        else:
            number2 = False

        calculation(operation, number1, number2)

        if calculate_again():
            reset_screen()
            continue
        else:
            break

    print_prompt(current_lang('bye'))

# Main Body
play()
