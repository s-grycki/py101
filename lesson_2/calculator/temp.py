# Welcome the user and give config operations
# Ask the user for the first number
# Check if valid numeric
# Ask the user for the second number
# Check if valid numeric
# Ask the user for an operation to perform
# Check if valid operator
# Perform the operation on the two numbers
# Print the result to the terminal as float
# Ask if user wants another calculation. Ask for first number if yes
# Else, exit program with message

import pdb
import json
import os
import operator
import math

with open('calculator.json', 'r') as file:
    data = json.load(file)

LANG = 'en'

# Function Declarations
def print_prompt(message):
    print(f'==> {message}')

def input_prompt(message):
    return input(f'==> {message}')

def reset_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def get_number(order):
    while True:
        number = input_prompt(f"What's the {order} number? ")

        if invalid_number(number):
            print_prompt(data[LANG]['invalid_number'])
        else:
            return float(number)

def get_operator():
    while True:
        operation = input_prompt(data[LANG]['operation'])
        
        if invalid_operator(operation):
            print_prompt(data[LANG]['invalid_operator'])
        elif zero_division(operation):
            print_prompt(data[LANG]['zero_error'])
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

def zero_division(operation):
    return operation == '4' and number2 == 0

def calculation():
    match operation:
        case '1':
            print_prompt(f'The result is: {number1 + number2}')
        case '2':
            print_prompt(f'The result is: {number1 - number2}')
        case '3':
            print_prompt(f'The result is: {number1 * number2}')
        case '4':
            print_prompt(f'The result is: {number1 / number2}')
        case '5':
            print_prompt(f'The result is: {number1 ** number2}')
        case '6':
            print_prompt(f'The result is: {math.exp(number1)}')
        case '7':
            print_prompt(f'The result is: {math.log(number1)}')
        case '8':
            print_prompt(f'The result is: {math.sqrt(number1)}')
        case '9':
            print_prompt(f'The result is: {math.cbrt(number1)}')

def calculate_again():
    answer = input_prompt(data[LANG]['do_again']).lower()
    return True if answer in data[LANG]['yes'] else False

def play():
    while True:
        print_prompt(data[LANG]['welcome'])
        answer = input_prompt(data[LANG]['config'])

        if answer in data[LANG]['round']:
            change_rounding()
        elif answer in data[LANG]['lang']:
            change_lang()
        else:
            break

    main_loop()

def change_rounding():
    answer = input_prompt(data[LANG]['change_rounding'])

    while True:
        try:
            int(answer)
        except ValueError:
            print_prompt(data[LANG]['invalid_number'])
        else:
            data['round_value'] = abs(answer)
            break

def change_lang():
    answer = input_prompt(data[LANG]['change_lang']).lower()

        while True:
            if answer in data['languages']:
                data['lang'] = answer
                break
            else:
                print_prompt(data[LANG]['lang_error'])

def main_loop():
    while True:
        operation = get_operator()
        number1 = get_number('first')
        if operation in data['operators']['valid'][:4]:
            number2 = get_number('second')
        calculation()

        if calculate_again():
            reset_screen()
            continue
        else:
            break

    print_prompt(data[LANG]['bye'])

# Main Body
print_prompt(data[LANG]['welcome'])

while True:
    number1 = get_number('first')
    number2 = get_number('second')
    operation = get_operator()
    calculation()

    if calculate_again():
        reset_screen()
        continue
    else:
        break

print_prompt(data[LANG]['bye'])
