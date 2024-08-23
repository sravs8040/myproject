from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Student, Parent, Attendance, Subject
from .forms import AttendanceForm, StudentForm, ParentForm, SubjectForm
from django.contrib.auth.decorators import login_required


# Home Page
def home(request):
    return render(request, 'index.html')


# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    return render(request, 'login.html')


# Super Admin Panel Views
@login_required
def manage_students(request):
    students = Student.objects.all()
    return render(request, 'manage_students.html', {'students': students})


@login_required
def manage_parents(request):
    parents = Parent.objects.all()
    return render(request, 'manage_parents.html', {'parents': parents})


@login_required
def manage_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'manage_subjects.html', {'subjects': subjects})


# Attendance Management Views
@login_required
def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    else:
        form = AttendanceForm()
    return render(request, 'create_attendance.html', {'form': form})

@login_required
def view_attendance(request):
    attendances = Attendance.objects.all()
    return render(request, 'view_attendance.html', {'attendances': attendances})


@login_required
def update_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'update_attendance.html', {'form': form})


@login_required
def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('view_attendance')
    return render(request, 'delete_attendance.html', {'attendance': attendance})


# Student Management Views
@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_students')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})


@login_required
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('manage_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('manage_students')
    return render(request, 'delete_student.html', {'student': student})


# Parent Management Views
@login_required
def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_parents')
    else:
        form = ParentForm()
    return render(request, 'create_parent.html', {'form': form})


@login_required
def update_parent(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('manage_parents')
    else:
        form = ParentForm(instance=parent)
    return render(request, 'update_parent.html', {'form': form})


@login_required
def delete_parent(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        parent.delete()
        return redirect('manage_parents')
    return render(request, 'delete_parent.html', {'parent': parent})


# Subject Management Views
@login_required
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_subjects')
    else:
        form = SubjectForm()
    return render(request, 'create_subject.html', {'form': form})


@login_required
def update_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('manage_subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'update_subject.html', {'form': form})


@login_required
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('manage_subjects')
    return render(request, 'delete_subject.html', {'subject': subject})
