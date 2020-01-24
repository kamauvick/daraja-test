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



