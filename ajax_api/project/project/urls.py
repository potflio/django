# urls.py
from django.urls import path
from app import views

urlpatterns = [
    path('',views.form,name='form'),
    path('add/', views.add_student, name='add_student'),
    path('list/', views.list_students, name='list_students'),
    path('students/', views.filter_students, name='filter_students'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]
