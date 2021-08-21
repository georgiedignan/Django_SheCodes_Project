from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#model that I created in models.py
from .models import CustomUser


#UesrCreationForm already has username and email
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']