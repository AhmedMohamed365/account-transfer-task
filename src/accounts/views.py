from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Account

def import_accounts(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("This is not a CSV file")
        
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string)  # Skip header row
        for row in csv.reader(io_string, delimiter=','):
            _, created = Account.objects.update_or_create(
                account_number=row[0],
                defaults={'balance': row[1]}
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
        from_account_number = request.POST['from_account']
        to_account_number = request.POST['to_account']
        amount = float(request.POST['amount'])
        
        from_account = get_object_or_404(Account, account_number=from_account_number)
        to_account = get_object_or_404(Account, account_number=to_account_number)

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