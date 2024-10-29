from task1 import add_operation

def interface():
    while True:
        print('1 - Add new record in database')
        print('2 - Exit program')
        print('----------------------------')
        action = int(input('What would you like to do:'))
        if action == 1:
            add_operation(input('Input an appointmentL'), float(input('Input a sum of money:')), input('Input tine of operation:'))
        elif action == 2:
            print('Goodbye.')
            break
        else:
            print('Unknown action.')
            continue
