from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Account
import pandas as pd

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
                account_number=row['ID'],
                defaults={'name': row['Name'], 'balance': row['Balance']}
            )
        return redirect('account_list')
    
    return render(request, 'accounts/import.html')

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    return render(request, 'accounts/account_detail.html', {'account': account})

def transfer_funds(request):
    if request.method == 'POST':
        from_account_id = request.POST['from_account']
        to_account_id = request.POST['to_account']
        amount = Decimal(request.POST['amount'])
        
        from_account = get_object_or_404(Account, id=from_account_id)
        to_account = get_object_or_404(Account, id=to_account_id)

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            return redirect('account_list')
        else:
            return HttpResponse("Insufficient funds")
    
    accounts = Account.objects.all()
    return render(request, 'accounts/transfer.html', {'accounts': accounts})