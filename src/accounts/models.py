from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Account {self.name} - ID: {self.id}'
    
    def display_balance(self):
        return f'Account {self.name} - Balance: {self.balance}'