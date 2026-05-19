from django import forms
from .models import Task
from django.utils import timezone


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',"min":timezone.now().date().isoformat()}))
    class Meta:
        model = Task
        fields = ["title","due_date"]