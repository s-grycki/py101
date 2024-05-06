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

def prompt(message):
    print(f'==> {message}')

def input_format(message):
    return input(f'==> {message}')

def get_number(order):
    while True:
        number = input_format(f"What's the {order} number? ")

        if invalid_number(number):
            prompt("Hmm... that doesn't look like a valid number.")
        else:
            return float(number)

def get_operator():
    while True:
        operation = input_format('What operation would you like to perform?\n'
                                 '1) Add 2) Subtract 3) Multiply 4) Divide ')
        
        if invalid_operator(operation):
            prompt('You must choose 1, 2, 3, or 4')
        elif zero_division(operation):
            prompt('Cannot divide by 0') 
        else:
            return operation

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def invalid_operator(operation):
    return operation not in ['1', '2', '3', '4']

def zero_division(operation):
    return operation == '4' and number2 == 0

def calculation():
    match operation:
        case '1':
            prompt(f'The result is: {number1 + number2}')
        case '2':
            prompt(f'The result is: {number1 - number2}')
        case '3':
            prompt(f'The result is: {number1 * number2}')
        case '4':
            prompt(f'The result is: {number1 / number2}')


# main body
prompt('Welcome to Calculator!')
number1 = get_number('first')
number2 = get_number('second')
operation = get_operator()
calculation()
