from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

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
        return f'{self.phonenumber} has sent {self.amount} >> Transaction No: {self.mpesa_receipt_number}'

class C2BPayments(models.Model):
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    transaction_time = models.CharField(max_length=50, blank=True, null=True)
    transaction_amount = models.CharField(max_length=120, blank=True, null=True)
    business_short_code = models.CharField(max_length=50, blank=True, null=True)
    bill_ref_number = models.CharField(max_length=120, blank=True, null=True)
    invoice_number = models.CharField(max_length=120, blank=True, null=True)
    org_account_balance = models.CharField(max_length=120, blank=True, null=True)
    third_party_transaction_id = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    def __repr__(self):
        return f'{self.first_name} has paid {self.transaction_amount} to {self.business_short_code}.'
