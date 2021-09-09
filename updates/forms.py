from django import forms
from .models import Updates
from django.forms import ModelForm

class NewsCreateForm(ModelForm):

    class Meta:
        model = Updates
        fields = '__all__'

        widgets={
            'Tags':forms.CheckboxSelectMultiple()
        }

