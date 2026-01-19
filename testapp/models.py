from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
import misaka

# Create your models here.

class User(AbstractUser): #for authentication
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    name =  models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    student_profile_pic = models.ImageField(upload_to="testapp/student_profile_pic",blank=True)

    def get_absolute_url(self):
        return reverse("testapp:student_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['roll_no']


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Teacher')
    name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    teacher_profile_pic = models.ImageField(upload_to="testapp/teacher_profile_pic",blank=True)
    class_students = models.ManyToManyField(Student,through="StudentsInClass")

    def get_absolute_url(self):
        return reverse("testapp:teacher_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
        

class StudentMarks(models.Model):
    teacher = models.ForeignKey(Teacher,related_name='given_marks',on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name='marks',on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)
    marks_obtained = models.IntegerField()
    maximum_marks = models.IntegerField()

    def __str__(self):
        return self.subject_name
    
class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher,related_name="class_teacher" , on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="user_student_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ('teacher','student')# What does this mean? 👉 A student cannot be added twice to the same teacher’s class.

class MessageToTeacher(models.Model):
    student = models.ForeignKey(Student,related_name='student',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='teacher',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message) #The plain text message is converted into HTML using misaka.
        super().save(*args, **kwargs)  

    class Meta: #Meta is used to give extra instructions to Django about how this model should behave.
        ordering = ['-created_at'] #What does this mean? Data will be shown by default in descending order of created_at. - means latest first.
        unique_together = ('student','message')

class ClassNotice(models.Model):
    teacher = models.ForeignKey(Teacher,related_name='teacher',on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,related_name='class_notice')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message
    
    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['teacher','message']

class ClassAssignment(models.Model):
    student = models.ManyToManyField(Student,related_name='student_assignment')
    teacher = models.ForeignKey(Teacher,related_name='teacher',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    assignment_name = models.CharField(max_length=True)
    assignment = models.FileField(upload_to='assignments')

    def __str__(self):
        return self.assignment_name

    class Meta:
        ordering = ['-created_at']

class SubmitAssignment(models.Model):
    student = models.ForeignKey(Student,related_name="student_submit",on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name="teacher_submit",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    submitted_assignment = models.ForeignKey(ClassAssignment,related_name='submission_for_assignment',on_delete=True)
    submit = models.FileField(upload_to='Submission')

    def __str__(self):
        return "Submitted" +str(self.submitted_assignment.assignment_name)
    
    class Meta:
        ordering = ['-created_at']







