from django.contrib import admin
from .models import Student, Parent, Subject, Attendance

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Attendance)
