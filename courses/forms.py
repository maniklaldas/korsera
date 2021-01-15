from django import forms 

from courses.models import Course

class CourseCreationForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = [
            'title', 'instructor2', 'teaching_assistant', 'department', 'sub_areas',
            'description', 'outcomes', 'prerequisites', 'credits',
            'fee', 'duration', 'start_date', 'end_date', 'is_running', 'is_offered',
            'banner_image1', 'banner_image2', 
        ]
        
class CourseUpdationForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = [
            'title', 'teaching_assistant', 'department', 'sub_areas',
            'description', 'outcomes', 'prerequisites', 'credits',
            'duration', 'start_date', 'end_date', 'is_running', 'is_offered',
            'banner_image1', 'banner_image2', 
        ]