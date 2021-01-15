"""
Utility functions for user accounts
"""

import datetime

from accounts.models import Student, Instructor, TeachingAssistant

def calculate_age(dob):
    year_of_birth = dob.year
    current_year = datetime.date.today().year
    age = current_year - year_of_birth
    
    return age

def generate_student_id(student):
    current_year = str(datetime.date.today().year)
    db_id = str(student.id)
    student_id = "S" + current_year + (5-len(db_id))*"0" + db_id
    
    return student_id

def generate_instructor_id(instructor):
    initials = instructor.user.first_name[0] + instructor.user.last_name[0]
    db_id = str(instructor.id)
    instructor_id = "I" + initials + (4-len(db_id))*"0" + db_id
    
    return instructor_id

def generate_ta_id(ta):
    current_year = str(datetime.date.today().year)
    db_id = str(ta.id)
    ta_id = "T" + current_year + (5-len(db_id))*"0" + db_id
    
    return ta_id

def complete_student_registration(student, user):
    student.user = user
    student.name = user.get_full_name()
    student.age = calculate_age(student.dob)
    student.save()
    student.student_id = generate_student_id(student)
    
    user.save()
    student.save()
    
def complete_instructor_registration(instructor, user):
    instructor.user = user
    instructor.name = user.get_full_name()
    instructor.age = calculate_age(instructor.dob)
    instructor.save()
    instructor.instructor_id = generate_instructor_id(instructor)
    
    user.save()
    instructor.save()
    
def complete_ta_registration(ta, user):
    ta.user = user
    ta.name = user.get_full_name()
    ta.age = calculate_age(ta.dob)
    ta.save()
    ta.ta_id = generate_ta_id(ta)
    
    user.save()
    ta.save()