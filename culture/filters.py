from django import forms
from django_filters import CharFilter
from .models import Culture
import django_filters


class CultureFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label='Name')
    class Meta:
        model = Culture
        fields = ['name']