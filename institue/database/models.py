from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )
   
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    userid = models.IntegerField(primary_key=True, unique=True, default=10001)

class profile(models.Model):
    userid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    forget_token = models.CharField(max_length=100)

class Student(models.Model):
    userid = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.TextField()
    Study = models.TextField()
    yearofjoin = models.TextField()
    dob = models.DateField()
    personalphnoe = models.TextField()
    parentphone = models.TextField()
    school = models.TextField()
    profile_pic = models.ImageField(upload_to='media/profile_picture')

class Subject(models.Model):
    userid = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    english = models.TextField(null=True)
    math = models.TextField(null=True)
    science = models.TextField(null=True)
    socialscience = models.TextField(null=True)
    testdate = models.DateField()
    date = models.DateField(auto_now_add=True)

class Teacher(models.Model):
    userid = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.TextField()
    qual = models.TextField()
    yearofjoin = models.TextField()
    dob = models.DateField()
    personalphnoe = models.TextField()


    

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    notice = models.TextField()
    date = models.DateField(auto_now_add=True)

class Homepagepicture(models.Model):
    id = models.AutoField(primary_key=True)
    homepage_pic = models.ImageField(upload_to='media/homepage_picture')
    date = models.DateField(auto_now_add=True)

class Gallerypicture(models.Model):
    id = models.AutoField(primary_key=True)
    gallery_pic = models.ImageField(upload_to='media/gallery_picture')
    about = models.TextField()
    date = models.DateField(auto_now_add=True)

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    Notes = models.ImageField(upload_to='media/notes')
    about = models.TextField(default='physics')
    study = models.TextField()
    Subject = models.TextField()
    date = models.DateField(auto_now_add=True)

class Teacherpicture(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_pic = models.ImageField(upload_to='media/teacher_picture')
    name = models.TextField()
    qualification = models.TextField()
    date = models.DateField(auto_now_add=True)

class Tophomepage(models.Model):
    id = models.AutoField(primary_key=True)
    topper_pic = models.ImageField(upload_to='media/topper_picture')
    name = models.TextField()
    study = models.TextField()
    school = models.TextField()
    marks = models.TextField()
    date = models.DateField(auto_now_add=True)

class Topbackpage(models.Model):
    id = models.AutoField(primary_key=True)
    topper_pic = models.ImageField(upload_to='media/topper_picture')
    name = models.TextField()
    study = models.TextField()
    school = models.TextField()
    marks = models.TextField()
    date = models.DateField(auto_now_add=True)

class Testinomial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email =models.EmailField()
    phone = models.TextField()
    msg = models.TextField()
    date = models.DateField(auto_now_add=True)
    