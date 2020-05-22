from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    First_name=forms.CharField(max_length=100)
    Last_name=forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['First_name','Last_name','username', 'email',]