import sqlite3
from task1 import add_operation


def interface():
    while True:
        print('1 - Add new record in database')
        print('2 - Exit program')
        print('----------------------------')
        action = int(input('What would you like to do:'))
        if action == 1:
            try:
                add_operation(input('Input an appointment:'), float(input('Input a sum of money:')), input('Input tine of operation:'))
            except sqlite3.IntegrityError:
                print('Name is already exists in table. Try another one.')
        elif action == 2:
            print('Goodbye.')
            break
        else:
            print('Unknown action.')
            continue

interface()
