#Adding this comment for Test Purpose
import os

def initialize():
    if not os.path.exists('Expenses.txt'):
        with open('Expenses.txt', 'w') as file:
            file.write('Date, Amount, Category, Description\n')

initialize()
