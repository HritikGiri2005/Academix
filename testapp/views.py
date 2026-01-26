from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import View,TemplateView,ListView,DetailView,DeleteView,CreateView,UpdateView
from django.utils.decorators import method_decorator
from testapp.forms import UserForm,TeacherProfileForm

# Create your views here.


#teacher signup 
def TeacherSignUp(request):
    user_type = 'teacher'
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        teacher_profile_form = TeacherProfileForm(data = request.POST)

        if user_form.is_valid() and teacher_profile_form.is_valid():
        
         

