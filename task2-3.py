import sqlite3
from main import add_operation, add_type


def interface():
    while True:
        print('1 - Add new record in database')
        print('2 - Exit program')
        print('----------------------------')
        action = int(input('What would you like to do:'))
        if action == 1:
            try:
                add_type(input('Input an appointment'), float(input('Input sum of money:')), input('Input date/time of operation'),input('Input type:'))
            except sqlite3.IntegrityError:
                print('This record already exists. Try again.')
        elif action == 2:
            print('Goodbye.')
            break
interface()