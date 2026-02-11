from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'is_completed']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Enter task title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:ring-indigo-500', 
                'rows': 3,
                'placeholder': 'Detailed objective description...'
            }),
            'priority': forms.NumberInput(attrs={
                'class': 'w-full p-3 rounded-xl border border-slate-200 outline-none focus:ring-2 focus:ring-indigo-500', 
                'min': 1, 
                'max': 5
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'w-6 h-6 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500'
            }),
        }