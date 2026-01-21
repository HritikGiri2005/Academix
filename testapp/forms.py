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

#Teacher Profile Update form

class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Teacher
        fields = ['name','subject_name','email','phone','teacher_profile_pic']

#Student Registeration Form

class StudentProfileForm(models.ModelForm):
    class Meta():
        model = Student
        fields = ['name','roll_no','phone','email']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'answer'}),
            'roll_no' : forms.NumberInput(attrs={'class':'answer'}),
            'phone' : forms.NumberInput(attrs={'class':'answer'}),
            'email' : forms.EmailInput(attrs={'class':'answer'}),
        }

##Student profile update form
class StudentProfileUpdateForm(models.ModelForm):
    class Meta():
        model = Student
        fields = ['name','roll_no','email','phone','student_profile_pic']

##form for uploading and updating marks

class MarksForm(models.ModelForm):
    class Meta():
        model = StudentMarks
        fields = ['subject_name','marks_obtained','maximum_marks']

#Writing Message to teacher
class MessageForm(models.ModelForm):
    class Meta():
        model = MessageToTeacher
        fields = ['message']


