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

# Function Declarations
def print_prompt(message):
    print(f'==> {message}')

def input_prompt(message):
    return input(f'==> {message}')

def get_number(order):
    while True:
        number = input_prompt(f"What's the {order} number? ")

        if invalid_number(number):
            print_prompt("Hmm... that doesn't look like a valid number.")
        else:
            return float(number)

def get_operator():
    while True:
        operation = input_prompt('What operation would you like to perform?\n'
                                 '1) Add 2) Subtract 3) Multiply 4) Divide ')
        
        if invalid_operator(operation):
            print_prompt('You must choose 1, 2, 3, or 4')
        elif zero_division(operation):
            print_prompt('Cannot divide by 0') 
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
            print_prompt(f'The result is: {number1 + number2}')
        case '2':
            print_prompt(f'The result is: {number1 - number2}')
        case '3':
            print_prompt(f'The result is: {number1 * number2}')
        case '4':
            print_prompt(f'The result is: {number1 / number2}')

def calculate_again():
    answer = input_prompt('Would you like to do another calculation? ').lower()
    return True if answer in ['y', 'yes'] else False

# Main Body
print_prompt('Welcome to Calculator!')

while True:
    number1 = get_number('first')
    number2 = get_number('second')
    operation = get_operator()
    calculation()

    if calculate_again():
        continue
    else:
        break

print_prompt('Thank You for Using Calculator. Goodbye!')
