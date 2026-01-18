from django import forms
from testapp.models import * 
from django.contrib.auth.forms import UserCreationForm

# user login form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'answer'}),
            'password1': forms.PasswordInput(attrs={'class':'answer'}),
            'password2': forms.PasswordInput(attrs={'class':'answer'}),
        }

