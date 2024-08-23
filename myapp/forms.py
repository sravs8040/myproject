from django import forms
from .models import Attendance, Student, Parent, Subject


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'status']
        widgets = {
            'student': forms.Select(),
            'subject': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('Present', 'Present'), ('Absent', 'Absent')]),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'email', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'roll_number': forms.TextInput(attrs={'placeholder': 'Enter roll number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'course': forms.TextInput(attrs={'placeholder': 'Enter course'}),
        }


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['student', 'name', 'email', 'phone']
        widgets = {
            'student': forms.Select(),
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter subject name'}),
            'code': forms.TextInput(attrs={'placeholder': 'Enter subject code'}),
        }
