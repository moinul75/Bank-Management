from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from User.models import User
from django.db.models.signals import post_save
#choice fields 
ACCOUNT_TYPE = (
    ('activate','Active'),
    ('in_active','In_active')
)

MATARIAL_STATUS = (
    ('married','Married'),
    ('single','Single'),
    ('others','Others')
)

GENDER = (
    ('male','Male'),
    ('female','Female'),
    ('others','Others')
)

IDENTITY_TYPES = (
    ('national_id_card','National_id_card'), 
    ('driving_licence','Driving_licence'), 
    ('international_passport','International_passport')
)
# Create your models here.


#account created 
#fields are id,user,account_balence,account_number,account_id,pin_number,ref_code,acount_status,date,kyc_submitted,kyc_confirm ,recommanded_by 
class Account(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,max_length=10,editable=False,default=uuid.uuid4)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_balence = models.DecimalField(max_length=20,max_digits=10,decimal_places=2,default=0.00)
    account_number = ShortUUIDField(unique=True,length=10,max_length=25,prefix="219",alphabet="4596873525") #21978546556416546
    account_id = ShortUUIDField(unique=True,length=7,max_length=25,prefix="MOI",alphabet="4596RETYTOYX") #MOI464654996
    pin_number = ShortUUIDField(unique=True,length=4,max_length=7,alphabet="123456789")
    ref_code = ShortUUIDField(unique=True,length=5,max_length=7,alphabet ="aacgeo4592712")
    account_status = models.CharField(max_length=20,choices=ACCOUNT_TYPE,default='in_active')
    date = models.DateTimeField(auto_now_add=True)
    kyc_statue = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommanded_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True,related_name='account_recommand')
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f"{self.user}"
    
    
    
    
#creeate model for KYC 
class KYC(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,max_length=10,editable=False,default=uuid.uuid4)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account = models.OneToOneField(Account,on_delete=models.CASCADE,null=True,blank=True)
    fullname  = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_pic',default='defaults.png')
    marital_status = models.CharField(max_length=20,choices=MATARIAL_STATUS)
    gender = models.CharField(max_length=10,choices=GENDER)
    identity_type = models.CharField(max_length=100,choices=IDENTITY_TYPES)
    indetity_image = models.ImageField(upload_to='identity',blank=True,null=True)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150,blank=True,null=True)
    state = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    signature = models.ImageField(upload_to='signature')
    fax = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-date']
    
    def __str__(self) -> str:
        return self.fullname
    
    
    
    
    
    
#signal for auto create account with signup 
def create_account(sender,instance,created,**kwargs):
    if created:
        Account.objects.create(user=instance)
        
#save the user 
def save_account(sender,instance,**kwargs):
    instance.account.save()
    
    
#connect the post save 
post_save.connect(create_account,sender=User)
post_save.connect(save_account,sender=User)

      
        
        
    
    
    



