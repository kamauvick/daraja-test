from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

PACKAGE = (
    ('Single', 'Single'),
    ('Duo', 'Two People'),
    ('Fam', 'Family Package'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile.jpg', blank=True, upload_to='profile_pictures/')
    email= models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


    class Meta:
        db_table= 'profile'
        ordering = ('username',)

    def __repr__(self):
        return f'{self.username}'

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, username=instance.username)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class LNMOnline(models.Model):
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=120)
    result_code = models.IntegerField()
    result_desc = models.TextField()
    amount = models.FloatField()
    mpesa_receipt_number = models.CharField(max_length=15)
    balance = models.CharField(blank=True, null=True , max_length=12)
    transaction_date = models.DateTimeField()
    phonenumber = models.CharField(max_length=13)

    def __repr__(self):
        return f'{self.mpesa_receipt_number}'

class C2BPayments(models.Model):
    TransactionType = models.CharField(max_length=50, blank=True, null=True)
    TransID = models.CharField(max_length=30, blank=True, null=True)
    TransTime = models.CharField(max_length=50, blank=True, null=True)
    TransAmount = models.CharField(max_length=120, blank=True, null=True)
    BusinessShortCode = models.CharField(max_length=50, blank=True, null=True)
    BillRefNumber = models.CharField(max_length=120, blank=True, null=True)
    InvoiceNumber = models.CharField(max_length=120, blank=True, null=True)
    OrgAccountBalance = models.CharField(max_length=120, blank=True, null=True)
    ThirdPartyTransID = models.CharField(max_length=120, blank=True, null=True)
    MSISDN = models.CharField(max_length=25, blank=True, null=True)
    FirstName = models.CharField(max_length=50, blank=True, null=True)
    MiddleName = models.CharField(max_length=50, blank=True, null=True)
    LastName = models.CharField(max_length=50, blank=True, null=True)

    def __repr__(self):
        return f'{self.InvoiceNumber}'

