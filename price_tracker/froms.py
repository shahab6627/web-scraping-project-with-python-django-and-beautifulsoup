from django import forms
from django.forms import TextInput
from .models import ItmePrice
from django.contrib.auth.models import User


class ItmePriceModelForm(forms.ModelForm):
    
    class Meta:
        model = ItmePrice
        fields = ['url','user']
        
        widgets = {
            'user': TextInput(attrs={
                'class': "form-control",
                'type':'hidden',
                
                
                }),
        }

class UserRegForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password_confirmation']
        
        widgets = {

            'password': TextInput(attrs={
                'class': "form-control",
                'type':'password',
                
                
                }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    