from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from mpesa.models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'profile_pic', 'email', 'phone_number', )