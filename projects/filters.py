from django import forms
from django_filters import CharFilter
from .models import Projects
import django_filters


class ProjectFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label='Name')
    class Meta:
        model = Projects
        fields = ['name']