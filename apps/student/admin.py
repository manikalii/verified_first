from django.contrib import admin
from apps.student.models import Student, Language
# Register your models here.
admin.site.register(Language)
admin.site.register(Student)