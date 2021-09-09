from django import forms
from django.forms import ModelForm
from .models import Projects

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
