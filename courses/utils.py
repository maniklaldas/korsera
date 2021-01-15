"""
Utility functions for courses
"""
import datetime

from courses.models import Course, EnrolledStudent
from accounts.models import Student, Instructor
from courses.constants import DEPARTMENT_MAPPINGS

def generate_course_code(course):
    department = course.department
    dept_code = DEPARTMENT_MAPPINGS[department]
    db_code = course.id
    
    course_code = str(dept_code)+(4-len(str(db_code)))*"0" + str(db_code)
    
    return course_code

def generate_reg_no(student, course):
    reg_no = str(course.course_code) + str(student.student_id)
    return reg_no

def complete_course_creation(course):
    course.course_code = generate_course_code(course)
    course.save()
    
def register_student_in_course(student, course):
    reg_no = generate_reg_no(student, course)
    enrolled_student = EnrolledStudent(
        reg_no = reg_no,
        student = student,
        course = course,
        batch = course.current_batch
    )
    enrolled_student.save()
    
