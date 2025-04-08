from django import forms
from app.models import Student

class Checkboxform(forms.ModelForm):
    class meta:
        model = Student
        fields = ['name','skills','hobbies']
