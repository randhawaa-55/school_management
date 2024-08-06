from django import forms
from .models import Course
from students.models import Student
from teachers.models import Teacher

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'students', 'teacher']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }
