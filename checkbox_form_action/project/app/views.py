from django.shortcuts import render,redirect
from app.forms import Checkboxform
from app.models import Student;
# Create your views here.
def form(request):
    return render(request,"form.html")

def submit(request):
    if request.method == 'POST':
        hob = request.POST.getlist("hobbies")
        second = ','.join(hob)
        data = Student(
            name = request.POST.get('name'),
            skills = request.POST.get('skills'),
            hobbies = second

        )
        data.save()
        return redirect('/')