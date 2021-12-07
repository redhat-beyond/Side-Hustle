from django.contrib import admin

# Register your models here.

from .models import StudentProfile

admin.site.register(StudentProfile)
