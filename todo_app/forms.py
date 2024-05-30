from django import forms
from .models import Task

class tdForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','duedate','status']