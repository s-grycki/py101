# Libraries
import json
import os
from time import sleep

# Json File
with open('loan_calculator.json', 'r') as file:
    MESSAGES = json.load(file)

# Global Constants
MONTHS_IN_YEAR = 12
MIN_INPUT = 0
MAX_BORROW = 1_000_000_000_000

# <============ MESSAGE FUNCTIONS ============>
def reset_screen():
    if os.name == 'nt':
        os.system("cls") # Windows
    else:
        os.system("clear") # Mac/Linux

def print_prompt(message):
    print(f'==> {message}')

def input_prompt(message):
    if isinstance(message, list):
        message = format_message(message)

    return input(f'==> {message}' + '\n==> ').lower()

# Splits long json messages into seperate lines
def format_message(message):
    return '\n==> '.join(message)

# Formats final values before output to user
def format_values(amount, rate, payment):
    formatted = f'{amount:.2f},{rate:.2f},{payment:.2f}'
    return formatted.split(',')

def print_result(amount, rate, years, months, payment):
    amount, rate, payment = format_values(amount, rate, payment)

    print_prompt(f'Borrowing ${amount} at an APR of {rate}% '
                 f'over {years} years and {months} months:')

    print_prompt(f'Your monthly payment is: ${payment}')

# <============ DATA RETRIEVAL FUNCTIONS ============>
def get_loan_information():
    reset_screen()
    amount = get_loan_amount()
    reset_screen()
    yearly_rate = get_yearly_rate()
    reset_screen()
    years = get_years()
    months = get_months(years)
    reset_screen()
    return (amount, yearly_rate, years, months)

def get_loan_amount():
    while True:
        amount = input_prompt(MESSAGES['loan_amount']).strip('$')
        amount = amount.replace(',', '')

        if valid_loan_amount(amount):
            return round(float(amount), 2)

        reset_screen()
        print_prompt(MESSAGES['amount_error'])

def get_yearly_rate():
    while True:
        rate = input_prompt(MESSAGES['rate_amount']).strip('%')

        if valid_rate(rate):
            return float(rate)

        reset_screen()
        print_prompt(MESSAGES['rate_error'])

def get_years():
    while True:
        years = input_prompt(MESSAGES['year_amount'])

        if valid_year_amount(years):
            return int(years)

        reset_screen()
        print_prompt(MESSAGES['year_error'])

def get_months(years):
    while True:
        months = input_prompt(MESSAGES['month_amount'])

        if valid_month_amount(months) and valid_duration(years, months):
            return int(months)

        reset_screen()
        print_prompt(MESSAGES['month_error'])

def calculate_again():
    answer = input_prompt(MESSAGES['do_again'])
    return answer in ('y', 'yes')

# <============ VALIDATION FUNCTIONS ============>
def valid_loan_amount(amount):
    try:
        amount = float(amount)
    except ValueError:
        return False

    if amount <= MIN_INPUT or amount >= MAX_BORROW:
        return False

    return True

def valid_rate(rate):
    try:
        rate = float(rate)
    except ValueError:
        return False

    if rate not in range(0, 100):
        return False

    return True

def valid_year_amount(years):
    try:
        years = int(years)
    except ValueError:
        return False

    if years not in range(0, 100):
        return False

    return True

def valid_month_amount(months):
    try:
        months = int(months)
    except ValueError:
        return False

    if months not in range(0, 12):
        return False

    return True

# Checks for 0 years and 0 months edge-case
def valid_duration(years, months):
    return years > MIN_INPUT or int(months) > MIN_INPUT

# <============ CALCULATION FUNCTIONS ============>
def calculate_total_months(years, months):
    return (years * MONTHS_IN_YEAR) + months

def calculate_monthly_rate(yearly_rate):
    return (yearly_rate / 100) / MONTHS_IN_YEAR

def calculate_payments(amount, rate, duration):
    if rate == 0: # Allows for 0 interest calculation without error
        monthly_payment = amount / duration
    else:
        monthly_payment = amount * (rate / (1 - (1 + rate) ** (-duration)))
    return monthly_payment

# <============ MAIN PROGRAM LOGIC ============>
def start():
    print_prompt(MESSAGES['welcome'])
    sleep(3)

    while True:
        amount, yearly_rate, years, months = get_loan_information() 
        duration = calculate_total_months(years, months)
        monthly_rate = calculate_monthly_rate(yearly_rate)
        monthly_payment = calculate_payments(amount, monthly_rate, duration)

        print_result(amount, yearly_rate, years, months, monthly_payment)

        if not calculate_again():
            break

        reset_screen()

    print_prompt(MESSAGES['goodbye'])

start()
