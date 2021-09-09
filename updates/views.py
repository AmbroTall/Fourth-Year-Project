from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView,ListView,View
from .models import Updates
from django.urls import reverse_lazy
from .forms import NewsCreateForm
from advertisements.models import Advertisements
from projects.models import Projects
from vacancies.models import Houses
from culture.models import Culture
from facilities.models import Facilities
from .myFilter import UpdateFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def homepage(request):
    advertisements = Advertisements.objects.filter(home_advert=True)[0:8]
    updates = Updates.objects.filter(important=True).order_by('-date_created')[0:4]
    projects = Projects.objects.all().order_by('-date_published')[0:4]
    vacancies = Houses.objects.all().order_by('-date_created')[0:3]
    culture = Culture.objects.all().order_by('-date_created')[0:3]
    facilities = Facilities.objects.all().order_by('-date_created')[0:3]
    context = {
        'facilities':facilities,
        'culture':culture,
        'vacancies':vacancies,
        'projects':projects,
        'advertisements':advertisements,
        'updates':updates
    }
    return render(request, 'updates/home_page.html', context)


def DisplayNews(request):
    advertisements = Advertisements.objects.filter(news_advert=True)[0:8]
    updates = Updates.objects.all().order_by('-date_created')
    myFilter = UpdateFilter(request.GET, queryset=updates)
    updates = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(updates, 5)
    try:
        updates = paginator.page(page)
    except PageNotAnInteger:
        updates = paginator.page(1)
    except EmptyPage:
        updates = paginator.page(paginator.num_pages)


    context = {
        'updates': updates,
        'myFilter':myFilter,
        'advertisements': advertisements,
    }
    return render(request, 'updates/news_show.html', context)


class NewsDetails(DetailView):
    model = Updates
    context_object_name = 'update'
    template_name = 'updates/detail_news.html'

class CreateNews(CreateView):
    form_class = NewsCreateForm
    template_name = 'updates/news_create.html'
    success_url = reverse_lazy('updates:homepage')

class UpdateNews(UpdateView):
    model = Updates
    fields = '__all__'
    template_name = 'updates/new_update.html'
    success_url = reverse_lazy('updates:homepage')

class DeleteNews(DeleteView):
    model = Updates
    template_name = 'updates/delete_news.html'
    success_url = reverse_lazy('updates:homepage')





