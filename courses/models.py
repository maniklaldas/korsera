from django.db import models
from django.utils import timezone
from PIL import Image

from accounts.models import Student, Instructor, TeachingAssistant
from courses.constants import STATUS_CHOICES

class Course(models.Model):
    """
    Course:
    """
    
    course_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=500)
    department = models.CharField(verbose_name="Subject Areas", max_length=200, default="")
    sub_areas = models.CharField(verbose_name="Sub Areas", max_length=200, default="")
    instructor1 = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name='instructor1')
    instructor2 = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name='instructor2', blank=True, null=True)
    teaching_assistant = models.ForeignKey(TeachingAssistant, on_delete=models.PROTECT, related_name='ta', blank=True, null=True)
    current_batch = models.CharField(max_length=10, default="1")
    
    description = models.TextField(max_length=10000, default="")
    outcomes = models.TextField(max_length=10000, default="")
    prerequisites = models.TextField(max_length=10000, default="")
    credits = models.IntegerField(default=3)
    
    fee = models.DecimalField(max_digits=7, decimal_places=2)   # Course Fee in INR
    duration = models.IntegerField(default=4)   # Course Duration in weeks
    start_date = models.DateField(auto_now=False, default=timezone.now, blank=True, null=True)
    end_date = models.DateField(auto_now=False, default=timezone.now, blank=True, null=True)
    is_running = models.BooleanField(default=False)
    is_offered = models.BooleanField(default=False)
    
    banner_image1 = models.ImageField(upload_to='media/course_images', default='default_course.png', blank=True, null=True)
    banner_image2 = models.ImageField(upload_to='media/course_images', default='default_course.png', blank=True, null=True)
    desc_file1 = models.FileField(upload_to='media/course_files', blank=True, null=True)
    desc_file2 = models.FileField(upload_to='media/course_files', blank=True, null=True)
    students_file = models.FileField(upload_to='media/course_files/students', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img1 = Image.open(self.banner_image1.path)
        img2 = Image.open(self.banner_image2.path)

        if img1 is not None and (img1.height>800 or img1.width > 1000):
            output_size = (800, 1000)
            img1.thumbnail(output_size)
            img1.save(self.banner_image1.path)
            
        if img2 is not None and (img2.height>800 or img2.width > 1000):
            output_size = (800, 1000)
            img2.thumbnail(output_size)
            img2.save(self.banner_image2.path)


class EnrolledStudent(models.Model):
    """
    Enrolled Student:
    """
    
    reg_no = models.CharField(max_length=20, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    batch = models.CharField(max_length=10, default="")
    
    is_fees_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Pursuing")
    grade = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)    # Grade in Percentage
    
    remarks = models.TextField(max_length=2000, default="")  
    
    