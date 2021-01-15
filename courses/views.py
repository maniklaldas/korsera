from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from accounts.models import Student, Instructor
from courses.models import Course, EnrolledStudent
from courses.forms import CourseCreationForm, CourseUpdationForm
from courses.utils import *

"""
Course Creation View
"""
@login_required 
def create_course(request):
    
    instructor = Instructor.objects.get(user = request.user)
    
    if instructor is not None:    
        if request.method == "POST":
            
            form = CourseCreationForm(request.POST, request.FILES)
            
            if form.is_valid():
                course = form.instance
                course.instructor1 = instructor
                course.save()
                complete_course_creation(course)
                
                messages.success(request, f'Course Created!')
                return redirect('course_details', course.id)
            
        else:
            form = CourseCreationForm()
        
        context = {
            'instructor' : instructor,
            'form' : form
        }    
        
        return render(request, 'courses/create_course.htm', context)
    
    else:
        messages.error(request, f'You are not authorized to create a new course')
        return redirect('index')
             

"""
Course Updation View
"""
@login_required 
def update_course(request, pk):
    
    try:
        instructor = request.user.instructor
        course = get_object_or_404(Course, pk = pk)
        if instructor == course.instructor1 or instructor == course.instructor2:
            form = None
            if request.method == "POST":
                
                form = CourseUpdationForm(request.POST, request.FILES, instance=course)
                
                if form.is_valid():
                    course = form.instance
                    course.save()
                    
                    messages.success(request, f'Course Updated!')
                    return redirect('course_details', course.id)
                
            else:
                form = CourseUpdationForm(instance=course)
            
            context = {
                'instructor' : instructor,
                'form' : form
            }    
            
            return render(request, 'courses/update_course.htm', context)
    
        else:
            messages.error(request, f'You are not authorized to update a course')
            return redirect('index')
        
    except:
        messages.error(request, f'You are not authorized to update a course')
        return redirect('index')
    


"""
Browse Courses
"""
def all_courses(request):
    
    courses = Course.objects.all(is_offered=True)
    
    context = {
        'courses' : courses
    }
    
    return render(request, 'courses/all_courses.htm', context) 
   
"""
Course Details View
"""
def course_details(request, pk):
    course = get_object_or_404(Course, pk = pk)
    
    context = {
        'course' : course
    }
    
    return render(request, 'courses/course_details.htm', context)

"""
Course Registration View
"""
@login_required
def course_registration(request, pk):

    course = get_object_or_404(Course, pk = pk)
    try:
        student = get_object_or_404(Student, user = request.user)
        course_students = EnrolledStudent.objects.all().filter(course = course)
        for stud in course_students:
            if student == stud.student:
                messages.success(request, f'You are already registered in this course')
                return redirect('index')
          
        register_student_in_course(student, course)
        return redirect('index')
            
    except:
        messages.error(request, f'You cannot register for this course')
        return redirect('index')
    
"""
Student Course Dashboard View
"""
@login_required
def student_course_dashboard(request, pk):
    
    
    student = request.user.student
    course = get_object_or_404(Course, pk = pk)
    enrolled_student = EnrolledStudent.objects.all().filter(student = student, course = course)[0]
    print(150)
    print(enrolled_student)
    context = {
        'student' : student,
        'course' : course,
        'en_student' : enrolled_student
    }
    print(157)
    return render(request, 'courses/student_course_dashboard.htm', context)
    '''except:
        messages.error(request, 'You cannot see dashboard for this course')
        return redirect('index')'''
    
"""
Instructor Course Dashboard View
"""
@login_required
def instructor_course_dashboard(request, pk):
    
    try:
        instructor = request.user.instructor
        course = get_object_or_404(Course, pk = pk)
        students = EnrolledStudent.objects.filter(course = course).count()

        if instructor == course.instructor1 or instructor == course.instructor2:
           
            context = {
                'instructor' : instructor,
                'course' : course,
                'students' : students
            }
            
            return render(request, 'courses/instructor_course_dashboard.htm', context)
    except:
        messages.error(request, 'You cannot see dashboard for this course')
        return redirect('index')
    
"""
All Courses
"""
def view_courses(request):
    courses = Course.objects.all().filter(is_offered = True)
    context = {
        'courses' : courses
    }
    
    return render(request, 'courses/view_courses.htm', context)

"""
Fee Payment
"""
def pay_fees(request, pk):
    course = get_object_or_404(Course, pk = pk)
    
    context = {
        'course' : course
    }
    
    return render(request, 'courses/pay_fees.htm', context)
