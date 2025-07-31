import os

def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('Date,Amount,Category,Description\n')

def add_expense(date, amount, category, description):
    with open('expenses.txt', 'a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    print('Expense added')

def view_expenses():
    with open('expenses.txt', 'r') as file:
        print(file.read())

def main():
    initialize_file()
    while True:
        print('1. Add Expense\n2. View Expenses\n3. Exit')
        choice = input('Select one: ')
        if choice == '1':
            date = input('Date (YYYY-MM-DD): ')
            amount = input('Amount: ')
            category = input('Category: ')
            description = input('Description: ')
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
