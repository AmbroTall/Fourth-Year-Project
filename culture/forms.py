from django import forms
from django.forms import ModelForm
from .models import Culture

class CreateCultureForm(forms.ModelForm):
    class Meta:
        model = Culture
        fields = '__all__'
