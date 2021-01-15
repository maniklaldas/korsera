from django.urls import path
from courses.views import *

urlpatterns = [
    path('new/', create_course, name='create_course'),
    path('<int:pk>/update', update_course, name='update_course'),
    path('all', view_courses, name='view_courses'),
    path('<int:pk>/', course_details, name='course_details'),
    path('<int:pk>/register', course_registration, name='course_registration'),
    path('<int:pk>/students/dashboard', student_course_dashboard, name='student_course_dashboard'),
    path('<int:pk>/instructors/dashboard', instructor_course_dashboard, name='instructor_course_dashboard'),
    
    path('create/', create_course, name='create_course'),
    path('<int:pk>/update/', update_course, name='update_course'),
]
