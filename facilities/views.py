from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from .models import Facilities
from .forms import CreateFacilitiesForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import FacilitiesFilter

def FacilitiesListView(request):
    projects = Facilities.objects.all().order_by('-date_created')
    myFilter = FacilitiesFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(projects, 5)
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
    return render(request, 'facilities/facilities_list.html', context)




class FacilitiesDetailView(DetailView):
    model = Facilities
    template_name = 'facilities/facilities_detail.html'
    context_object_name = 'projects'

class FacilitiesCreateView(CreateView):
    form_class = CreateFacilitiesForm
    template_name = 'facilities/create_facilities.html'
    success_url = reverse_lazy('facilities:facilities_home')


class UpdateFacilitiesView(UpdateView):
    model = Facilities
    fields = '__all__'
    template_name = 'facilities/update_facilities.html'
    success_url = reverse_lazy('facilities:facilities_home')

class DeleteFacilitiesView(DeleteView):
    model = Facilities
    template_name = 'facilities/delete_facilities.html'
    success_url = reverse_lazy('facilities:facilities_home')



