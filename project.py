import json
import os
from datetime import datetime

DATA_FILE = 'budget_data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': []}


def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def add_entry(data, entry_type):
    description = input(f"Enter {entry_type} description: ")
    amount = float(input(f"Enter amount for {description}: "))
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    data[entry_type].append({'description': description, 'amount': amount, 'date': date_str})


def show_balance(data):
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    balance = total_income - total_expenses
    print(f"\nTotal Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")


def list_transactions(data):
    print("\n--- Income ---")
    for item in data['income']:
        print(f"{item['date']}: {item['description']} - ${item['amount']:.2f}")
    print("\n--- Expenses ---")
    for item in data['expenses']:
        print(f"{item['date']}: {item['description']} - ${item['amount']:.2f}")
    print()


def main():
    data = load_data()
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. List All Transactions")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_entry(data, 'income')
        elif choice == '2':
            add_entry(data, 'expenses')
        elif choice == '3':
            show_balance(data)
        elif choice == '4':
            list_transactions(data)
        elif choice == '5':
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
