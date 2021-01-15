from django.contrib import admin
from accounts.models import Student, Instructor

admin.site.register([Student, Instructor])

# Register your models here.
