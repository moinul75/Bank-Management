from django.urls import path 
from User import views


urlpatterns = [
    path('signup',views.Signup, name='signup')
]
