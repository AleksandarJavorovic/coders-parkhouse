import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coders_parkhouse')

business = SHEET.worksheet('business')

business_data = business.get_all_values()


def welcome_function():
    '''
    Welcoming message on the entrance to the parkhouse.
    '''
    print('\nHello there and welcome to the Coders Parkhouse.\n')

driver = ''

def drivers_choice():
    '''
    Function which offers 2 choices for the driver.
    Driver can park or leave the parking lot.
    Function also handles possible errors and returns
    the driver to chose between 1 and 2.
    '''
    print('What would you like to do?\n1. Park the car\n2. Leave the parking lot\n')
    try:
        driver = input('Please enter 1 or 2: ')
        driver_int = int(driver)
        if driver_int == 1:
            parking_prices()
            parking_decision()
            enter_regplate()
        elif driver_int == 2:
            print('I would like to leave the parking lot')
        elif driver_int != 1 and driver_int != 2:
            print(f'\nYou typed in: {driver_int}, that\'s not an option try again.\n')
            return drivers_choice()
    except ValueError: #handling te errors in case the answer is not an integer
        print(f'\nYou typed in: {driver}, you must choose between numbers 1 and 2.\n')
        return drivers_choice()


def parking_prices():
    '''
    This function is simply presenting needed info to the
    customer, informing him of the prices and possible penalties.
    '''
    print('\n\nOk, rules are following:\n')
    print('1. Each started hour means you need to pay for the whole hour.\n')
    print('2. You need to enter for how many hours you want to park.\n')
    print('3. Price per hour is 3€.\n')
    print('4. If you exceed your time, each next hour is 5€.\n')
    print('Are you ok with it?\n')
    print('Answer with "yes" to continue or "no" to reject.\n')


def parking_decision():
    '''
    Function which alows driver to accept the terms of the parking lot
    or to refuse them and leave before parking.
    '''
    drivers_answer = input(': ')
    drivers_answer_lower = drivers_answer.lower()
    try:
        if drivers_answer_lower == 'yes':
            print('\n\nWith that in mind, we are going to need your registration number.')
        elif drivers_answer_lower == 'no':
            farewell_message()
        elif drivers_answer_lower != 'yes' and drivers_answer_lower != 'no':
            print('\nPlease answer with "yes" or "no".\n') 
            parking_decision()
    except:
        quit()

def farewell_message():
    '''
    Function which prints out farewell message and exits the program
    '''
    print('\nHave a nice day! Until the next time! :)\n')
    quit()


# Pattern of the regplates to enter
reg_plates_pattern = '[A-Z]{2,4}[-][0-9]{3,5}[-][A-Z]{2}'

# List to contain driver's details
driver_details = []


def enter_regplate():
    '''
    Here you must enter your regplate number using
    one of the already defined patterns.
    '''
    reg_plates = ''
    print('\nPlese use one of the following patterns:\n')
    print('1. XY-1234-XY\n2. XY-123-XY\n3. XYZ-1234-XY\n4. XYZ-123-XY')
    print('\nX,Y,Z representing any UPPERCASE letter [A-Z].')
    print('\nFor the numbers section use digits [0-9].')
    print('\nDon\'t forget dashes where needed.')
    reg_plates = input('\nEnter registration number: ')
    if (re.search(reg_plates_pattern, reg_plates)):# Line validating the registration number
        print('\nRegistration number is valid!\n')
        driver_details.insert(0, reg_plates)
        print(driver_details)
    else:
        print('\nSorry, that doesn\'t look like any of the patterns provided.')
        return enter_regplate()


def main():
    '''
    Main function of the code. It hosts the other functions.
    '''
    welcome_function()
    drivers_choice()
    

main()