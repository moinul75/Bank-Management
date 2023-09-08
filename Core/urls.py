from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('search_account/',views.search_user,name='search_user'),
    path('amount_pay/<account_user>/',views.payment_send,name='amount_pay')
]
