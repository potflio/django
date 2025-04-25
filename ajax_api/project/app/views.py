from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        student = Student.objects.create(name=name, age=age)
        return JsonResponse({'status': 'success', 'id': student.id})

def list_students(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)

def form(request):
    return render(request,"form.html")

@csrf_exempt
def delete_student(request, id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({'status': 'deleted'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

@csrf_exempt
def update_student(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            student = Student.objects.get(id=id)
            student.name = data.get('name', student.name)
            student.age = data.get('age', student.age)
            student.save()
            return JsonResponse({'status': 'updated'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

def filter_students(request):
    age = request.GET.get('age')  
    if age:
        students = list(Student.objects.filter(age=age).values())
    else:
        students = list(Student.objects.all().values())
    return JsonResponse(students, safe=False)