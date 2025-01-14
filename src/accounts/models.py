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