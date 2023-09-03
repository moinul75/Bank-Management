from django.shortcuts import render,redirect
from User.forms import UserRegistrationForm
from User.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_form  = form.save()
            username = form.cleaned_data.get("username")  
            messages.success(request, f"hey {username}, your account is registered successfully...")  
            user_form = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request,user_form)    
            return redirect('index')
    elif request.user.is_authenticated:
        messages.warning(request, f"you are already logged in")
        return redirect('index')
    else:
        form = UserRegistrationForm()
        
    context = {
        'form':form
    }
        
    return render(request, 'signup.html',context)

