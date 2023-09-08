from django.urls import path 
from User import views

app_name = 'User'

urlpatterns = [
    path('sign_up',views.Signup, name='signup'),
    path('sign_in',views.Login, name='login'),
    path('logout',views.LogOut,name='logout'),
]
