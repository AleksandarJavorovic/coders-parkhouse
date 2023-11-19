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

# Pattern of the regplates to enter.
reg_plates_pattern = '[A-Z]{2,4}[-][0-9]{3,5}[-][A-Z]{2}'

# Pattern for parking duration.
initial_time_pattern = '^\\d+$'

# Pattern for plus sign.
plus_minus_pattern = '^[+]+$'

# List to contain driver's details.
driver_details = []

# List to help present information to the driver.
parking_info = ['Registration','Number of hours', 'Initial cost in €']

def parking_prices():
    '''
    This function is simply presenting needed info to the
    customer, informing him of the prices and possible penalties.
    '''
    print('\n\nOk, rules are following:\n')
    print('1. Each started hour means you need to pay for the whole hour.')
    print('2. You need to enter for how many hours you want to park.')
    print('3. Price per hour is 3€.')
    print('4. If you exceed your time, each next hour is 5€.')
    print('Are you ok with it?')
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
    Function which prints out farewell message and exits the program.
    '''
    print('\nHave a nice day! Until the next time! :)\n')
    quit()


def parking_info_presentation():
    '''
    Function to present info to the driver.
    Registration number, duration and price.
    '''
    driver_details_display = {parking_info[i]: driver_details[i] for i in range(len(parking_info))}
    print(driver_details_display)


def initial_time_function():
    '''
    Function to set initial duration of parking.
    '''
    print('For how long are you planning to park?\n')
    print('Minimal number of hours is 1.\n')
    initial_time = input('Number of hours: ')
    try:
        if int(initial_time) == 0:
            print('\nZero is not an option, sorry.\n')
            initial_time_function()
        elif (re.search(initial_time_pattern, initial_time)) and int(initial_time) > 0:
            driver_details.insert(1, initial_time) # adding initial_time to the list
            print('\nVery well!')
            print('\nTry not to be late, otherwise it will be more expensive.')
            print('\nYour parking details are:\n')
            
        elif (re.findall("[+-]", initial_time)): # insuring there are no +/- prefixes
            print('\nDon\'t use plus/minus signs as prefix.\n')
            initial_time_function()
    except ValueError: # handling invalid inputs
        print('\nUse only didigts 0-9, only whole numbers please and no special signs.\n')
        initial_time_function()
    

def initial_price_calculation():
    '''
    Function to calculate initial price of the parking
    according to the inital parking time.
    '''
    initial_price = str(int(driver_details[1]) * 3) # Calculating initial price.
    driver_details.insert(2, initial_price)


def save_driver_detials():
    '''
    Function to save parking info to the google sheet.
    '''
    business.append_row(driver_details)


def return_to_parkinglot():
    '''
    Function which brings the driver to the entrance
    of the parking lot again or lets him leave.
    '''
    print('\n\nType in "RETURN", to return to the parking lot to pick up your car.')
    print('If you aren\'t ready to pick up your car yet, type in "NOT YET".')
    driver_returns = input(': ')
    if driver_returns.upper() == 'RETURN':
        drivers_choice() # Starting the program again.
    elif driver_returns.upper() == 'NOT YET':
        print('\nOk, see ya later!\n')
        quit()
    else:
        print('\nInvalid input.\n')
        return_to_parkinglot()


def enter_regplate():
    '''
    Here you must enter your regplate number using
    one of the already defined patterns.
    '''
    reg_plates = ''
    print('\nPlease use one of the following patterns:')
    print('1. XY-1234-XY\n2. XY-123-XY\n3. XYZ-1234-XY\n4. XYZ-123-XY')
    print('\nX,Y,Z representing any UPPERCASE letter [A-Z].')
    print('For the numbers section use digits [0-9].')
    print('Don\'t forget dashes where needed.')
    existing_regplates = business.col_values(1) # List of registration numbers within the sheet
    reg_plates = input('\nEnter registration number: ')
    if reg_plates not in existing_regplates:# checking the list of existing reg. numbers
        if (re.search(reg_plates_pattern, reg_plates)):# Line validating the registration pattern.
            print('\n\nRegistration number is valid!\n')
            driver_details.insert(0, reg_plates) # Adding reg_plates to the list.
        else:
            print('\nSorry, that doesn\'t look like any of the patterns provided.')
            return enter_regplate()
    else:
        print('\nRegistration number is already in our system!\n')
        print('You either have to pay for your parking time')
        print('or re-enter your reg. number if you made a mistake.')
        reg_check()


def reg_check():
    '''
    Function to run when registration is already existing
    '''
    print('\nWrong input!')
    print('To pay your bill type in "proceed".\nTo enter new reg-number type in "new".')
    reg_plate_check = input(': ')
    if reg_plate_check == 'proceed':
        print('I want to pay my bill!')
        quit()
    elif reg_plate_check == 'new':
        enter_regplate()
    else:
        reg_check()



def drivers_choice():
    '''
    Function which offers 2 choices for the driver.
    Driver can park or leave the parking lot.
    Function also handles possible errors and returns
    the driver to chose between 1 and 2.
    '''
    print('\nHello there and welcome to the Coders Parkhouse.\n')
    print('What would you like to do?\n1. Park the car\n2. Leave the parking lot\n')
    try:
        driver = input('Please enter 1 or 2: ')
        driver_int = int(driver)

        if (re.findall("[+]", driver)):
            print('\nDon\'t use prefix plus.\n')
            drivers_choice()
        elif driver_int == 1:
            parking_prices() # Calling list of the rules and prices.
            parking_decision()
            enter_regplate()
            initial_time_function()
            initial_price_calculation()
            parking_info_presentation()
            save_driver_detials()
            return_to_parkinglot()
        elif driver_int == 2:
            print('I would like to leave the parking lot')
        elif driver_int != 1 and driver_int != 2:
            print(f'\nYou typed in: {driver_int}, that\'s not an option try again.\n')
            drivers_choice()
    except ValueError: # Handling te errors in case the answer is not an integer.
        print(f'\nYou typed in: {driver}, you must choose between numbers 1 and 2.\n')
        drivers_choice()

drivers_choice()