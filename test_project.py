import unittest
import os
import json
from budget_tracker import (
    load_data,
    save_data,
    add_income,
    add_expense,
    get_total_income,
    get_total_expenses,
    get_balance,
    get_transactions
)

TEST_FILE = 'test_budget_data.json'

class TestPersonalBudgetTracker(unittest.TestCase):

    def setUp(self):
        # Ensure test file is clean before each test
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        # Initialize with empty data
        self.data = {'income': [], 'expenses': []}

    def tearDown(self):
        # Clean up test file after each test
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_load_and_save_data(self):
        # Save data and then load it back
        save_data(self.data, TEST_FILE)
        loaded_data = load_data(TEST_FILE)
        self.assertEqual(loaded_data, self.data)

    def test_add_income(self):
        add_income(self.data, 'Salary', 3000)
        self.assertEqual(len(self.data['income']), 1)
        self.assertEqual(self.data['income'][0]['amount'], 3000)

    def test_add_expense(self):
        add_expense(self.data, 'Groceries', 150)
        self.assertEqual(len(self.data['expenses']), 1)
        self.assertEqual(self.data['expenses'][0]['amount'], 150)

    def test_get_total_income(self):
        add_income(self.data, 'Salary', 3000)
        add_income(self.data, 'Freelance', 500)
        total_income = get_total_income(self.data)
        self.assertEqual(total_income, 3500)

    def test_get_total_expenses(self):
        add_expense(self.data, 'Rent', 1000)
        add_expense(self.data, 'Utilities', 200)
        total_expenses = get_total_expenses(self.data)
        self.assertEqual(total_expenses, 1200)

    def test_get_balance(self):
        add_income(self.data, 'Salary', 3000)
        add_expense(self.data, 'Groceries', 150)
        balance = get_balance(self.data)
        self.assertEqual(balance, 2850)

    def test_get_transactions(self):
        add_income(self.data, 'Salary', 3000)
        add_expense(self.data, 'Groceries', 150)
        transactions = get_transactions(self.data)
        self.assertEqual(len(transactions), 2)
        self.assertIn('Salary', transactions[0]['description'])
        self.assertIn('Groceries', transactions[1]['description'])

if __name__ == '__main__':
    unittest.main()
