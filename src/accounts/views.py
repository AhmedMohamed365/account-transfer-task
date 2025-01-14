from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Account, Transaction
import pandas as pd

from django.contrib import messages
from django.db import transaction


def import_accounts(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension not in ['csv', 'xlsx', 'txt']:
            return HttpResponse("Unsupported file type")

        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
        elif file_extension == 'xlsx':
            df = pd.read_excel(uploaded_file)
        elif file_extension == 'txt':
            df = pd.read_csv(uploaded_file, delimiter='\t')

        for _, row in df.iterrows():
            Account.objects.update_or_create(
                id=row['ID'],
                defaults={'name': row['Name'], 'balance': row['Balance']}
            )
        return redirect('account_list')
    
    return render(request, 'accounts/import.html')

def account_list(request):
    search_query = request.GET.get('search', '')
    order_by = request.GET.get('order_by', 'balance')
    accounts = Account.objects.all()
    if search_query:
        accounts = accounts.filter(name__icontains=search_query)

    if order_by:
        accounts = accounts.order_by(order_by)

    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, id):
    account = get_object_or_404(Account, id=id)
    outgoing_transactions = Transaction.objects.filter(from_account=account).order_by('-date')
    incoming_transactions = Transaction.objects.filter(to_account=account).order_by('-date')
    return render(request, 'accounts/account_detail.html',
                   {'account': account,
                    'incoming_transactions':incoming_transactions,
                    'outgoing_transactions':outgoing_transactions})



@transaction.atomic
def transfer_funds(request):
    if request.method == 'POST':
        
        from_account_id = request.POST['from_account']
        to_account_id = request.POST['to_account']
        amount = Decimal(request.POST['amount'])
        # Server-side validation for amount
        if amount <= 0:
            messages.error(request, 'Amount must be greater than 0.')
            return redirect('transfer_funds')
        
        from_account = get_object_or_404(Account, id=from_account_id)
        to_account = get_object_or_404(Account, id=to_account_id)

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            # Create a transaction record
            Transaction.objects.create(
                from_account=from_account,
                to_account=to_account,
                amount=amount
            )
            messages.success(request, f'Transfer completed successfully.\nYour balance is now {from_account.balance}')
        else:
            messages.error(request, 'Insufficient funds.')
    
    accounts = Account.objects.all() 
    return render(request, 'accounts/transfer.html', {'accounts': accounts})