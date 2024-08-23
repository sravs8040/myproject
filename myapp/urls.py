from django.urls import path
from . import views


urlpatterns = [
    # Attendance URLs
    path('create/', views.create_attendance, name='create_attendance'),
    path('', views.view_attendance, name='view_attendance'),
    path('update/<int:pk>/', views.update_attendance, name='update_attendance'),
    path('delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),

    # Student URLs
    path('students/update/<int:pk>/', views.update_student, name='update_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('students/create/', views.create_student, name='create_student'),

    # Parent URLs
    path('parents/update/<int:pk>/', views.update_parent, name='update_parent'),
    path('parents/delete/<int:pk>/', views.delete_parent, name='delete_parent'),
    path('parents/create/', views.create_parent, name='create_parent'),


]
