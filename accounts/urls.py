from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_student, name='register_student'),
    
    path('instructor/register/', register_instructor, name='register_instructor'),
    
    path('profile/', student_profile, name='student_profile'),
    
    path('instructor/profile/', instructor_profile, name='instructor_profile'),
    
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.htm'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='main/index.htm'), name='logout'),
]
