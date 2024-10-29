import sqlite3
from datetime import datetime
from locale import currency

import requests

connection = sqlite3.connect('monobank.db')

cursor = connection.cursor()


def create_table_bank():
    query = '''
    CREATE TABLE IF NOT EXISTS Bank (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_name TEXT,
    currency_value REAL,
    current_date DATETIME
    )
    '''
    cursor.execute(query)


create_table_bank()


response = requests.get('https://api.monobank.ua/bank/currency')
print(f'Connetcion status: {response.ok}')
print(response.text)

resp_json = response.json()


def insert_data(name: str, value: float, date: str):
    query = '''
    INSERT INTO Bank (currency_name, currency_value, current_date) VALUES (?, ?, ?);
    '''
    cursor.execute(query,[name, value, date])
    connection.commit()

for info in resp_json:
    name = info.get('currencyCodeA')
    value = info.get('rateBuy')
    date = info.get('date')
    date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    insert_data(name, value, date)