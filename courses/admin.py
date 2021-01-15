from django.contrib import admin
from courses.models import Course, EnrolledStudent

admin.site.register([Course, EnrolledStudent])

# Register your models here.
