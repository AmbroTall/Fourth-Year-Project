from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from .models import Culture
from .forms import CreateCultureForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import CultureFilter
from django.contrib.auth.mixins import LoginRequiredMixin


def CultureListView(request):
    projects = Culture.objects.all().order_by('-date_created')
    myFilter = CultureFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(projects, 4)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page('1')
    except EmptyPage:
        projects = paginator.page(paginator.num_page)


    context = {
        'projects':projects,
        'myFilter':myFilter,
    }
    return render(request, 'culture/culture_list.html', context)




class CultureDetailView(LoginRequiredMixin,DetailView):
    model = Culture
    template_name = 'culture/culture_detail.html'
    context_object_name = 'projects'

class CultureCreateView(CreateView):
    form_class = CreateCultureForm
    template_name = 'culture/create_culture.html'
    success_url = reverse_lazy('culture:culture_home')


class UpdateCultureView(UpdateView):
    model = Culture
    fields = '__all__'
    template_name = 'culture/update_culture.html'
    success_url = reverse_lazy('culture:culture_home')

class DeleteCultureView(DeleteView):
    model = Culture
    template_name = 'culture/culture_delete.html'
    success_url = reverse_lazy('culture:culture_home')




