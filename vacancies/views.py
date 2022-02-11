from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView,DeleteView,UpdateView
from .models import Houses
from advertisements.models import Advertisements
from .forms import HouseVacancyForm
from django.urls import reverse_lazy
from .filters import VacancyFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin

def HouseListView(request):
    advertisements = Advertisements.objects.filter(house_advert=True)[0:8]
    hous = Houses.objects.all().order_by('-date_created')
    myFilter = VacancyFilter(request.GET, queryset=hous)
    projects = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(projects, 4)
    try:
        hous = paginator.page(page)
    except PageNotAnInteger:
        hous = paginator.page(1)
    except EmptyPage:
        hous = paginator.page(paginator.num_page)


    context = {
        'hous':hous,
        'myFilter':myFilter,
        'advertisements': advertisements,
    }
    return render(request, 'vacancies/house_list.html', context)

class HouseDetailView(LoginRequiredMixin,DetailView):
    model = Houses
    template_name = 'vacancies/house_detail.html'
    context_object_name = 'house'

class HouseCreate(CreateView):
    form_class = HouseVacancyForm
    template_name = 'vacancies/vacancy_create_form.html'
    success_url = reverse_lazy('vacancies:vacancy_home')


class HouseUpdateForm(UpdateView):
    model = Houses
    fields = '__all__'
    template_name = 'vacancies/vacancy_update.html'
    success_url = reverse_lazy('vacancies:vacancy_home')

class HouseDeleteView(DeleteView):
    model = Houses
    template_name = 'vacancies/vacancy_delete.html'
    success_url = reverse_lazy('vacancies:vacancy_home')


