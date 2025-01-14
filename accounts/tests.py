from django.test import TestCase
from .models import Account
import csv
from django.core.files.storage import FileSystemStorage

class AccountModelTest(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(account_number='123456', balance=1000.00)
        self.account2 = Account.objects.create(account_number='654321', balance=500.00)

    def test_account_creation(self):
        self.assertEqual(self.account1.account_number, '123456')
        self.assertEqual(self.account1.balance, 1000.00)

    def test_account_balance_update(self):
        self.account1.balance += 200.00
        self.account1.save()
        self.assertEqual(self.account1.balance, 1200.00)

class AccountTransferTest(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(account_number='123456', balance=1000.00)
        self.account2 = Account.objects.create(account_number='654321', balance=500.00)

    def test_transfer_funds(self):
        self.account1.transfer_funds(self.account2, 200.00)
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 800.00)
        self.assertEqual(self.account2.balance, 700.00)

    def test_transfer_funds_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account1.transfer_funds(self.account2, 1200.00)

class CSVImportTest(TestCase):

    def test_import_accounts_from_csv(self):
        csv_file = 'path/to/accounts.csv'  # Update with the actual path
        with open(csv_file, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                Account.objects.create(account_number=row[0], balance=float(row[1]))

        accounts = Account.objects.all()
        self.assertEqual(accounts.count(), expected_count)  # Replace expected_count with the actual number of accounts in the CSV file