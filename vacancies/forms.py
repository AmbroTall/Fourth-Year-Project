from django.forms import ModelForm
from django import forms
from .models import Houses

class HouseVacancyForm(forms.ModelForm):
    class Meta:
        model = Houses
        fields = '__all__'
        ordering:['-date_created']

        widgets={
            'tags':forms.CheckboxSelectMultiple()
        }