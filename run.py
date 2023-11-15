import gspread
from google.oauth2.service_account import Credentials

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
    '''
    print('What would you like to do?\n1. Park the car\n2. Leave the parking lot\n')
    try:
        driver = input('Please enter 1 or 2: ')
        driver_int = int(driver)
        if driver_int == 1:
            print('I would like to park the car')
        elif driver_int == 2:
            print('I would like to leave the parking lot')
        elif driver_int != 1 and driver_int != 2:
            print(f'\nYou typed in {driver_int}, that\'s not an option try again.\n')
            return drivers_choice()
    except ValueError:
        print(f'\nYou typed in: {driver}, you must choose between numbers 1 and 2.\n')
        return drivers_choice()
        
    


def main():
    '''
    Main function of the code. It hosts all the other functions.
    '''
    welcome_function()
    drivers_choice()

main()