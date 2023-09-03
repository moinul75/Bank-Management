from django.contrib import admin
from Account.models import Account
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AccountAdmin(ImportExportModelAdmin):
    #list_display, editable, search_list 
    list_display = ['user','account_id','account_status','account_balence','date']
    list_editable = ['account_status','account_balence']
    list_filter = ['account_status']
    
    
admin.site.register(Account,AccountAdmin)

