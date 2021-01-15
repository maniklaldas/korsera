from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Student, Instructor, TeachingAssistant

class UserRegistrationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        
class StudentProfileForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['phone', 'address', 'college', 'programme']   
        
class InstructorProfileForm(forms.ModelForm):
    
    class Meta:
        model = Instructor
        fields = ['name', 'phone', 'address', 'college', 'department', 'profile_link']  
        
class TAProfileForm(forms.ModelForm):
    
    class Meta:
        model = TeachingAssistant
        fields = ['name', 'phone', 'address', 'college', 'department', 'profile_link']
            