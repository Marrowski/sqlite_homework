import sqlite3

connection = sqlite3.connect('homework.db')

cursor = connection.cursor()

def create_table_money():
    query = '''
    CREATE TABLE IF NOT EXISTS Shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment VARCHAR(255) NOT NULL UNIQUE,
    sum REAL NOT NULL UNIQUE,
    time TEXT NOT NULL UNIQUE
    );
    '''

    cursor.execute(query)

create_table_money()


def add_operation(appointment: str, sum: float, time: str):
    query = '''
    INSERT INTO Shop(appointment, sum, time) VALUES(?,?,?);
    '''
    cursor.execute(query,[appointment, sum, time])
    connection.commit()


