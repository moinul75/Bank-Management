from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Account.models import Account
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

def search_user(request):
    #find all the user 
    account = Account.objects.all()
    
    #filter user by account_number and account_id
    query = request.POST.get('account_number') 
    
    if query:
        account = Account.objects.filter(
            Q(account_number = query)| Q(account_id = query)
        ).distinct()

        
    
    context = {
        'account':account,
        'query':query
    }
    
    return render(request,'search_account.html',context)

#paymaent send 
def payment_send(request,account_user):
    try:
        account = Account.objects.get(account_number = account_user)
        print(account)
    except: 
        messages.warning(request,f'User account is not found')
        
    context= {
        'account':account
    }
    
    return render(request,'amount_pay.html',context)

