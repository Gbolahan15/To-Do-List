from django import forms
from .models import Tasks

class TaskForm(forms.modelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'completed']