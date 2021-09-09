from django import forms
from django_filters import CharFilter
from .models import Houses
import django_filters


class VacancyFilter(django_filters.FilterSet):
    location = CharFilter(field_name='location', lookup_expr="icontains", label='Location')
    class Meta:
        model = Houses
        fields = ['location']