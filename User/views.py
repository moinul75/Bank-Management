from django.shortcuts import render,redirect
from User.forms import UserRegistrationForm
from User.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_form  = form.save()
            username = form.cleaned_data.get("username")  
            messages.success(request, f"hey {username}, your account is registered successfully...") 
            return redirect('User:login')
    elif request.user.is_authenticated:
        messages.warning(request, f"you are already logged in")
        return redirect('index')
    else:
        form = UserRegistrationForm()
        
    context = {
        'form':form
    }
        
    return render(request, 'signup.html',context)


#login 
def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #check auth
        try: 
            user = authenticate(email=email,password=password)
            if user is None:
                messages.warning(request,f"Username or eamil is not found!!")
                return redirect('User:login')
            else:
                login(request,user)
                messages.success(request, f"You Are Logged in Successfully..")
                return redirect('index')
        except:
            pass               
    return render(request,'login.html')




#logout
@login_required
def LogOut(request):
    logout(request)
    messages.success(request,f"Logged Out Successfully")
    return redirect('User:signup')


