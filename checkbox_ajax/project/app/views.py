from django.shortcuts import render,redirect
from app.forms import Checkboxform
from app.models import Student;
import ast
# Create your views here.
def form(request):
    return render(request,"form.html")

def submit(request):
    if request.method == 'POST':
        hob = request.POST.get("hobbies")
        print(hob)
        string_list = ast.literal_eval(hob)
        print(string_list)
        final_data = ','.join(string_list)
        print(final_data)
        data = Student(
            name = request.POST.get('name'),
            skills = request.POST.get('skills'),
            hobbies = final_data

        )
        data.save()
        return redirect('/')