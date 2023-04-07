from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(AuthenticationForm):
  username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form__input'}))
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
  
class RegisterForm(UserCreationForm):
  username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'form__input'}))
  password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form__input'}))
  password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class': 'form__input'}))
  email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class': 'form__input'}))
  class Meta:
    model = User
    fields = ("username", "password1","password2", "email")
  
class RequestForm(forms.ModelForm):
  class Meta:
    model = Personal
    fields = "__all__"  
  
class GroupRequestForm(forms.ModelForm):
  class Meta:
    model = Group
    fields = "__all__"  