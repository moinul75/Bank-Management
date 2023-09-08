from django.urls import path 
from Account.views import KycRegistration,AccountView

app_name = 'Account'

urlpatterns = [
    path('kyc_regi',KycRegistration, name='kyc_regi'),
    path('dashboard/', AccountView, name='dash_board'),

]
