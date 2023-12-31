import gspread
from google.oauth2.service_account import Credentials
import re

# This part of code is taken from Love Sandwiches project
###############################################################
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coders_parkhouse')
###############################################################

business = SHEET.worksheet('business')  # google sheet

existing_regplates = business.col_values(1)

# Pattern of the regplates to enter.
reg_plates_pattern = '^[A-Z]{2,3}[-][0-9]{3,4}[-][A-Z]{2}$'

# Pattern for parking duration.
time_pattern = '^\\d+$'

# List to contain driver's details.
driver_details = []

# List to help present information to the driver.
parking_info = ['Registration:', 'Hours:', 'Price in €:']


def parking_prices():
    '''
    This function is simply presenting needed info to the
    customer, informing him of the prices and possible penalties.
    '''
    print('\n\nOk, rules are following:\n')
    print('1. You need to enter for how many hours you want to park.')
    print('2. Price per hour is 3€.')
    print('3. Hours dictate minimal amount which you will have to pay.')
    print('4. If you exceed your time, penalty fee of 10€ will be applied.')
    print('Are you ok with it?')
    print('Answer with "yes" to continue or "no" to reject.')


def parking_decision():
    '''
    Function which alows driver to accept the terms of the parking lot
    or to refuse them and leave before parking.
    '''
    drivers_answer = input('\n: ')
    drivers_answer_lower = drivers_answer.lower()
    try:
        if drivers_answer_lower == 'yes':
            print('\n\nWe are going to need your registration number.')
        elif drivers_answer_lower == 'no':
            farewell_message()
        elif drivers_answer_lower != 'yes' and drivers_answer_lower != 'no':
            print('\nPlease answer with "yes" or "no".\n')
            parking_decision()
    except ValueError:
        quit()


def farewell_message():
    '''
    Function which prints out farewell message and exits the program.
    '''
    print('\nHave a nice day! Until the next time! :)')
    print(r''' ___   _     ____      ___   _     ____
| |_) \ \_/ | |_      | |_) \ \_/ | |_
|_|_)  |_|  |_|__     |_|_)  |_|  |_|__ ''')
    quit()


def parking_info_presentation(data):
    '''
    Function to present info to the driver.
    Registration number, duration and price.
    '''
    for i in range(3):
        print(parking_info[i], data[i])


def initial_time_function():
    '''
    Function to set initial duration of parking.
    '''
    print('For how long are you planning to park?\n')
    print('Minimal number of hours is 1.\n')
    initial_time = input('Number of hours\n: ')
    try:
        if int(initial_time) == 0:
            print('\nZero is not an option, sorry.\n')
            initial_time_function()
        elif (re.search(time_pattern, initial_time)) and int(initial_time) > 0:
            # adding initial_time to the list
            driver_details.insert(1, initial_time)
            print('\nVery well!')
            print('\nTry not to be late, otherwise it will be more expensive.')
            print('\nYour parking details are:\n')
        # insuring there are no +/- prefixes
        elif (re.findall("[+-]", initial_time)):
            print('\nDon\'t use plus/minus signs as prefix.\n')
            initial_time_function()
    except ValueError:  # handling invalid inputs
        print('\nUse only didigts 0-9, only whole numbers please.')
        print('No special signs neither.\n')
        initial_time_function()


def initial_price_calculation():
    '''
    Function to calculate initial price of the parking
    according to the inital parking time.
    '''
    initial_price = str(int(driver_details[1]) * 3)  # Calc. initial price.
    driver_details.insert(2, initial_price)  # inserting price into the list


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
    print('\n\nType in "RETURN", to return to pick up your car.')
    print('If you aren\'t ready to pick up your car yet, type in "NOT YET".')
    driver_returns = input('\n: ')
    if driver_returns.upper() == 'RETURN':
        drivers_choice()  # Starting the program again.
    elif driver_returns.upper() == 'NOT YET':
        print('\nOk, see ya later!\n')
        quit()  # quiting the program
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
    # List of registration numbers within the sheet
    existing_regplates = business.col_values(1)
    reg_plates = input('\nEnter registration number\n: ')
    if reg_plates not in existing_regplates:
        # validating the reg. pattern.
        if (re.search(reg_plates_pattern, reg_plates)):
            print('\n\nRegistration number is valid!\n')
            # Add reg_plates to the list.
            driver_details.insert(0, reg_plates)
        else:
            print('\nSorry, invalid input!')
            return enter_regplate()
    else:
        print('\nRegistration number is already in our system!\n')
        print('You either have to pay your debt')
        print('to be able to park here again')
        print('or re-enter your reg. number if you made a mistake.')
        reg_check(reg_plates)


def reg_check(data):
    '''
    Function to run when registration is already existing
    '''
    print('\nTo pay your debt type in "pay".')
    print('To enter new reg-number type in "new".')
    existing_regplates = business.col_values(1)
    reg_plate_check = input('\n: ')
    if reg_plate_check == 'pay':
        print('\nPaying...')
        # finding index of reg. num row
        reg_row_index = existing_regplates.index(data) + 1
        # deleting reg. number row from sheet
        reg_row = business.delete_rows(reg_row_index)
        print('\nOk now you can park here again.\n')
        enter_regplate()
    elif reg_plate_check == 'new':
        enter_regplate()
    else:
        print('\nInvalid input!')
        print(f'Sorry, but "{reg_plate_check}" is not an option.')
        return reg_check(data)


def enter_regplate_leave():
    '''
    Function to be run before exiting the parking lot.
    Checking for the existing registration number.
    '''
    existing_regplates = business.col_values(1)
    print('\nWe need your registration number please.')
    reg_plates = input('\n: ')
    if (re.search(reg_plates_pattern, reg_plates)):  # cheking the pattern
        # checking if regplates are already present
        if reg_plates in existing_regplates:
            print('\nValid Input!')
            print('\nDetails loading...\n')
            request_list(reg_plates)
        # regplates aren't present in the sheet
        elif reg_plates not in existing_regplates:
            print('\nRegistration number is valid but not in our system.')
            print('Are you sure that you parked here?')
            print('1. "Yes" I am sure(type in your reg. number again)')
            print('2. "No", looks like I made a mistake. o.O')
            print('Yes or no please.')
            reg_check_two()
    else:
        print('\nInvalid data, please use correct pattern.')
        enter_regplate_leave()


def reg_check_two():
    '''
    Recursive function in case user doesn't answer
    with yes or no.
    '''
    drivers_answer = input('\n: ')
    drivers_answer_lower = drivers_answer.lower()
    if drivers_answer_lower == 'yes':
        enter_regplate_leave()
    elif drivers_answer_lower == 'no':
        farewell_message()
    elif drivers_answer_lower != 'yes' and drivers_answer_lower != 'no':
        print('\nPlease answer with "yes" or "no".\n')
        reg_check_two()


def request_list(data):
    '''
    Function to pull the list from google sheet
    according to the registration number.
    It will retrieve registration number,
    initial parking time and initial price.
    '''
    existing_regplates = business.col_values(1)
    reg_row_index = existing_regplates.index(data) + 1  # row index
    reg_row = business.row_values(reg_row_index)  # google sheet row
    parking_info_presentation(reg_row)
    final_price_count(reg_row)


def final_price_count(data):
    '''
    Function to count final price according
    to the final duration of parking.
    '''
    initial_time = data[1]
    initial_price = data[2]
    print(f'\nYour initial duration was {initial_time} hours.')
    print('\nYou arrived(select one scenario):')
    print('1. Earlier\n2. On point\n3. Later')
    print('Type in 1, 2, or 3.')
    real_duration = input('\n: ')
    real_duration_len = len(real_duration)
    try:
        # taking care there are no other characters besides 1,2 or 3.
        if real_duration_len > 1:
            print("\nInvalid input! No empty spaces, no special signs.")
            final_price_count(data)
        # earlier
        elif int(real_duration) == 1:
            final_price = initial_price  # earlier
            print(f'\nYour final price should be {final_price}€.\n')
            driver_coder(data, final_price)
        # on point
        elif int(real_duration) == 2:
            final_price = initial_price  # on point
            print(f'\nYour final price should be {final_price}€.\n')
            driver_coder(data, final_price)
        # later
        elif int(real_duration) == 3:
            final_price = str(int(initial_price) + 10)  # later
            print(f'\nYour final price should be {final_price}€.\n')
            driver_coder(data, final_price)
        # none of the above options
        elif int(real_duration) != [1, 2, 3]:
            print('\nThat\'s not an option.')
            final_price_count(data)
    except ValueError:
        print('Invalid input!')
        final_price_count(data)


def driver_coder(data, price):
    '''
    Function to ask our driver if he works for
    CODE INSTITUTE or not, and maybe apply small
    discount if the answer is positive and the
    driver knows the secret code. :)
    '''
    print('Hey, one thing I want to tell you.')
    print('I think you work for Code Institute.')
    print('Do you know about the code for 10⁒ discount')
    print('we gave them long time ago?')
    print('If you know it, type it in and save yourself few euros.')
    print('If you don\'t, type in anything to skip to the payment.')
    print('(Shhhh, its: CI2023)')
    check_coder = input('\n: ')
    if check_coder.upper() == 'CI2023':
        # calc. discounted final price
        final_price_cor = int(price) - int(price) * 0.1
        print('\nLooks like your boss likes you! :)')
        print(f'\nYour final price is {final_price_cor}€.\n')
        pay_at_exit(data)
    else:
        final_price_cor = price
        print('\nLooks like your boss doesn\'t like you so much. :(')
        print(f'\nSorry, you still need to pay {final_price_cor}€.\n')
        pay_at_exit(data)


def pay_at_exit(data):
    '''
    Function to pay the final price at the exit
    and quit the program.
    '''
    print('To pay, type in "pay".')
    final_payment = input('\n: ')
    if final_payment.lower() == 'pay':
        print('Paying...')
        existing_regplates = business.col_values(1)
        reg_row_index = existing_regplates.index(data[0]) + 1  # row index
        business.delete_rows(reg_row_index)  # deleting google sheet row
        print('Complete!')
        farewell_message()
    else:
        print('\nSorry, until you pay, you can\'t drive out! :)')
        pay_at_exit(data)


def drivers_choice():
    '''
    Function which offers 2 choices for the driver.
    Driver can park or leave the parking lot.
    Function also handles possible errors and returns
    the driver to chose between 1 and 2.
    '''
    print(r''' __    ___   ___   ____  ___   __
/ /`  / / \ | | \ | |_  | |_) ( (`
\_\_, \_\_/ |_|_/ |_|__ |_| \ _)_)''')
    print(r''' ___    __    ___   _     _     ___   _     __   ____
| |_)  / /\  | |_) | |_/ | |_| / / \ | | | ( (` | |_
|_|   /_/--\ |_| \ |_| \ |_| | \_\_/ \_\_/ _)_) |_|__ ''')
    print('\nHello there and welcome to the Coders Parkhouse.\n')
    print('What would you like to do?')
    print('1. Park the car\n2. Leave the parking lot\n')
    try:
        driver = input('Please enter 1 or 2\n: ')
        driver_int = int(driver)

        if (re.findall('[\\s +]', driver)):
            print('\nInvalid input!\n')
            drivers_choice()
        elif driver_int == 1:
            parking_prices()  # Calling list of the rules and prices.
            parking_decision()
            enter_regplate()
            initial_time_function()
            initial_price_calculation()
            parking_info_presentation(driver_details)
            save_driver_detials()
            '''
            Clearing drivers_details list to prevent multiple
            lists being written into the sheet if we choose the same
            registration number after "return" in the end of the program.
            '''
            driver_details.clear()
            return_to_parkinglot()
        elif driver_int == 2:
            enter_regplate_leave()
        elif driver_int != 1 and driver_int != 2:
            print(f'\nYou typed in: {driver_int}')
            print('That\'s not an option try again.\n')
            drivers_choice()
    except ValueError:  # Handling ValueErrors
        print(f'\nYou typed in: {driver}')
        print('You must choose between numbers 1 and 2.\n')
        drivers_choice()


drivers_choice()
