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


def main():
    '''
    Main function of the code.
    '''
    welcome_function()

main()