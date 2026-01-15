from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

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
