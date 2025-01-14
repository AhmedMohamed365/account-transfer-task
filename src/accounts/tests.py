from django.test import TestCase
from django.urls import reverse
from .models import Account, Transaction
from decimal import Decimal
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile

class AccountModelTest(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(id=uuid.uuid4(), name='Ahmed', balance=1000.00)
        self.account2 = Account.objects.create(id=uuid.uuid4(), name='Jane Doe', balance=500.00)

    def test_account_creation(self):
        self.assertIsInstance(self.account1.id, uuid.UUID)
        self.assertEqual(self.account1.name, 'Ahmed')
        self.assertEqual(self.account1.balance, 1000.00)

    def test_account_balance_update(self):
        self.account1.balance += 200.00
        self.account1.save()
        self.assertEqual(self.account1.balance, 1200.00)

class AccountTransferTest(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(id=uuid.uuid4(), name='John Doe', balance=1000.00)
        self.account2 = Account.objects.create(id=uuid.uuid4(), name='Jane Doe', balance=500.00)

    def test_transfer_funds(self):
        response = self.client.post(reverse('transfer_funds'), {
            'from_account': self.account1.id,
            'to_account': self.account2.id,
            'amount': '200.00'
        })
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 800)
        self.assertEqual(self.account2.balance, 700.00)
        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.from_account, self.account1)
        self.assertEqual(transaction.to_account, self.account2)
        self.assertEqual(transaction.amount, Decimal('200.00')) 

    def test_insufficient_funds(self):
        response = self.client.post(reverse('transfer_funds'), {
            'from_account': self.account2.id,
            'to_account': self.account1.id,
            'amount': '600.00'
        })
        self.account2.refresh_from_db()
        self.assertEqual(self.account2.balance, 500.00)  # Balance should remain unchanged
        self.assertEqual(Transaction.objects.count(), 0)

class AccountImportTest(TestCase):

    def test_import_accounts(self):
        csv_content = """ID,Name,Balance
        123456,John Doe,1000.00
        654321,Jane Doe,500.00
        """
        uploaded_file = SimpleUploadedFile("accounts.csv", csv_content.encode('utf-8'), content_type="text/csv")

        response = self.client.post(reverse('import_accounts'), {
            'file': uploaded_file
        }, format='multipart')
        self.assertEqual(response.status_code, 302)  # Redirect after successful import
        self.assertEqual(Account.objects.count(), 2)
        self.assertEqual(Account.objects.get(name='John Doe').balance, Decimal('1000.00'))
        self.assertEqual(Account.objects.get(name='Jane Doe').balance, Decimal('500.00'))