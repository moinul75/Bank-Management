from django.contrib import admin
from Account.models import Account,KYC
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AccountAdmin(ImportExportModelAdmin):
    #list_display, editable, search_list 
    list_display = ['user','account_id','account_status','account_balence','date']
    list_editable = ['account_status','account_balence']
    list_filter = ['account_status']


class KYCAdmin(ImportExportModelAdmin):
    search_fields = ['fullname']
    list_display = ['user','fullname']
        
    
admin.site.register(Account,AccountAdmin)
admin.site.register(KYC,KYCAdmin)


