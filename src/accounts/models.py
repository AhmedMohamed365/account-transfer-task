import uuid
from django.db import models



class Account(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.name} - ID: {self.id}'
    
    # def display_balance(self):
    #     return f'{self.name} - Balance: {self.balance}'

class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='outgoing_transactions', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='incoming_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction from {self.from_account.name} to {self.to_account.name} - Amount: {self.amount}'