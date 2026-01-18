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

##Teacher Registeration form

class TeacherProfileForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name','subject_name','phone','email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'answer'}),
            'subject_name': forms.TextInput(attrs={'class':'answer'}),
            'phone':forms.NumberInput(attrs={'class':'answer'}),
            'email':forms.EmailInput(attrs={'class':'answer'}),
        }

