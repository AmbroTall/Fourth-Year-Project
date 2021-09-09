from django import forms
from django_filters import CharFilter
from .models import Facilities
import django_filters


class FacilitiesFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label='Name')
    class Meta:
        model = Facilities
        fields = ['name']