from django.contrib.auth.forms import UserCreationForm
from User.models import User 


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        