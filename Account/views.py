from django.shortcuts import render,redirect
from .forms import KYCForm
from .models import Account,KYC
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#account 
@login_required
def AccountView(request):
    if request.user.is_authenticated: 
        try:
           Kyc = KYC.objects.get(user=request.user)
        except: 
            Kyc= None
            messages.warning(request, f'You Should Submit your Kyc Before Access to the Account page')
            return redirect('Account:kyc_regi')
        account = Account.objects.get(user=request.user)
    else:
        messages.error(request, f"You Must Logged in to access this page and Dashboard")
        return redirect('User:login')
    
    context = {
        'account': account, 
        'Kyc' : Kyc
    }
    return render(request, 'account.html',context)





# Create your views here.
@login_required
def KycRegistration(request):
    #find the user and account 
    user = request.user
    account = Account.objects.get(user=user)
    
    #get the kyc if crated 
    try:
        Kyc = KYC.objects.get(account=account)
    except: 
        Kyc = None
    #get form and save the valid form 
    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES, instance=Kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user  = user 
            new_form.account = account
            new_form.save()
            messages.success(request, "Kyc Submitted Successfully, Now In Review")
            return redirect('index')
        else:
            print(f"Form Errors: {form.errors}")
    else:
        form = KYCForm(instance=Kyc)
    
    context = {
        'account':account, 
        'form':form,
        'Kyc':Kyc
    }
    
    return render(request, 'kyc_registration.html',context)
            
    
    
