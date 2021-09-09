from django import forms
from django.forms import ModelForm
from .models import Facilities

class CreateFacilitiesForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = '__all__'
