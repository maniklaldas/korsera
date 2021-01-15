from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image 

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

class Student(models.Model):
    """
    Student Account: 
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    student_id = models.CharField(max_length=20, default="", unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    dob = models.DateField(auto_now=False, default=timezone.now)
    phone = models.CharField(max_length=15, default="+91-")
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default="Male")
    address = models.TextField(max_length=1000, default="")
    college = models.CharField(max_length=1000, default="")
    programme = models.CharField(max_length=200, default="")
    
    image = models.ImageField(upload_to='media/student_pics', default='default_user.png')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
            

class Instructor(models.Model):
    """
    Instructor Account:
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    instructor_id = models.CharField(max_length=20, default="", unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, default=timezone.now)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15, default="+91-")
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default="Male")
    address = models.TextField(max_length=1000, default="")
    college = models.CharField(max_length=1000, default="")
    department = models.CharField(max_length=200, default="")
    profile_link = models.CharField(max_length=500)
    
    image = models.ImageField(upload_to='media/student_pics', default='default_user.png')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

class TeachingAssistant(models.Model):
    """
    TA Account:
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    ta_id = models.CharField(max_length=20, default="", unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, default=timezone.now)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15, default="+91-")
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default="Male")
    address = models.TextField(max_length=1000, default="")
    college = models.CharField(max_length=1000, default="")
    department = models.CharField(max_length=200, default="")
    profile_link = models.CharField(max_length=500)
    
    image = models.ImageField(upload_to='media/student_pics', default='default_user.png')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)