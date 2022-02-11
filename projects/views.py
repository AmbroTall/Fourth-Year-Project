from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from .models import Projects
from .forms import CreateProjectForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProjectFilter
from django.contrib.auth.mixins import LoginRequiredMixin

def ProjectListView(request):
    projects = Projects.objects.all().order_by('-date_published')
    myFilter = ProjectFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(projects, 5)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_page)


    context = {
        'projects':projects,
        'myFilter':myFilter,
    }
    return render(request, 'projects/project_list.html', context)


class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Projects
    template_name = 'projects/project_detail.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    form_class = CreateProjectForm
    template_name = 'projects/create_project.html'
    success_url = reverse_lazy('projectss:project_home')


class UpdateProjectView(UpdateView):
    model = Projects
    fields = '__all__'
    template_name = 'projects/update_project.html'
    success_url = reverse_lazy('projectss:project_home')

class DeleteProjectView(DeleteView):
    model = Projects
    template_name = 'projects/delete_project.html'
    success_url = reverse_lazy('projectss:project_home')



