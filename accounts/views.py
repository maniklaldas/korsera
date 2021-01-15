from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

from accounts.models import Student, Instructor, TeachingAssistant
from courses.models import EnrolledStudent, Course
from accounts.forms import UserRegistrationForm, StudentProfileForm, InstructorProfileForm
from accounts.utils import *

def post_login(request):
    if request.user.is_superuser:
        return redirect('staff_dashboard')
    else:
        return redirect('student_dashboard')

"""
Student Registation View
"""
def register_student(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentProfileForm(request.POST)
        data = request.POST
        
        user = User(
            first_name = data["first_name"],
            last_name = data["last_name"],
            username = data["email"],
            email = data["email"],
            password = data["password1"],
        )
        user.set_password(data["password1"])
        user.save()

        username = data["email"]
        pwd = data["password1"]
        
        #auth_user = authenticate(username=username, password=user.password)
        #login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')

        student = Student.objects.create(
            user = user,
            student_id=data["email"],
            phone=data["phone"],
            address = data["address"],
            college = data["college"],
            programme = data["programme"],
        )
        student.save()
              
        complete_student_registration(student, user)
        student.save()
        
        return redirect('index')
    else:
        user_form = UserRegistrationForm()
        student_form = StudentProfileForm()
    
    context = {
        'uform' : user_form,
        'form' : student_form
    }
    
    return render(request, 'accounts/register_student.htm', context)

"""
Instructor Registation View
    - Permissions : Only Administrator Access
"""
@staff_member_required
def register_instructor(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        instructor_form = InstructorProfileForm(request.POST)
        data = request.POST
        
        user = User(
            first_name = data["first_name"],
            last_name = data["last_name"],
            username = data["email"],
            email = data["email"],
            password = data["password1"],
        )
        user.set_password(data["password1"])
        user.save()

        username = data["email"]
        pwd = data["password1"]
        
        #auth_user = authenticate(username=username, password=user.password)
        #login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')

        instructor = instructor.objects.create(
            user = user,
            instructor_id=data["email"],
            phone=data["phone"],
            address = data["address"],
            college = data["college"],
            department = data["department"],
        )
        instructor.save()
              
        complete_instructor_registration(instructor, user)
        instructor.save()
        
        return redirect('index')
    else:
        user_form = UserRegistrationForm()
        instructor_form = InstructorProfileForm()
    
    context = {
        'uform' : user_form,
        'form' : instructor_form
    }
    
    return render(request, 'accounts/register_instructor.htm', context)

"""
TA Registation View
    - Permissions : Only Administrator and Instructor Access
"""
@login_required
def register_ta(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        ta_form = TAProfileForm(request.POST)
        data = request.POST
        
        user = User(
            first_name = data["first_name"],
            last_name = data["last_name"],
            username = data["email"],
            email = data["email"],
            password = data["password1"],
        )
        user.set_password(data["password1"])
        user.save()

        username = data["email"]
        pwd = data["password1"]
        
        #auth_user = authenticate(username=username, password=user.password)
        #login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')

        ta = TeachingAssistant.objects.create(
            user = user,
            ta_id=data["email"],
            phone=data["phone"],
            address = data["address"],
            college = data["college"],
            department = data["department"],
        )
        ta.save()
              
        complete_ta_registration(ta, user)
        ta.save()
        
        return redirect('index')
    else:
        user_form = UserRegistrationForm()
        ta_form = TAProfileForm()
    
    context = {
        'uform' : user_form,
        'form' : ta_form
    }
    
    return render(request, 'accounts/register_ta.htm', context)


"""
Student Profile Updation View
"""
@login_required 
def student_profile(request):
    
    student = get_object_or_404(Student, user = request.user)
    courses = EnrolledStudent.objects.all().filter(student = student)
    
    if request.method == "POST":
        
        form = StudentProfileForm(request.POST, request.FILES, instance = student)
        
        if form.is_valid():
            student = form.instance
            student.save()
            
            messages.success(request, f'Profile Updated!')
            return redirect('student_dashboard')
        
    else:
        form = StudentProfileForm(instance = student)
    
    context = {
        'student' : student,
        'courses' : courses,
        'form' : form
    }    
    
    return render(request, 'accounts/student_profile.htm', context)

"""
Instuctor Profile Updation View
"""
@login_required 
def instructor_profile(request):
    
    instructor = get_object_or_404(Instructor, user = request.user)
    courses = Course.objects.all().filter(Q(instructor1 = instructor) | Q(instructor2 = instructor))
    
    
    if request.method == "POST":
        
        form = InstructorProfileForm(request.POST, request.FILES, instance = instructor)
        
        if form.is_valid():
            instructor = form.instance
            instructor.save()
            
            messages.success(request, f'Profile Updated!')
            return redirect('instructor_dashboard')
        
    else:
        form = InstructorProfileForm(instance = instructor)
    
    context = {
        'instructor' : instructor,
        'form' : form,
        'courses' : courses,
    }    
    
    return render(request, 'accounts/instructor_profile.htm', context)

"""
TA Profile Updation View
"""
@login_required 
def ta_profile(request):
    
    ta = get_object_or_404(TeachingAssistant, user = request.user)
    
    if request.method == "POST":
        
        form = TAProfileForm(request.POST, request.FILES, instance = ta)
        
        if form.is_valid():
            ta = form.instance
            ta.save()
            
            messages.success(request, f'Profile Updated!')
            return redirect('ta_dashboard')
        
    else:
        form = TAProfileForm(instance = ta)
    
    context = {
        'ta' : ta,
        'form' : form
    }    
    
    return render(request, 'accounts/ta_profile.htm', context)
