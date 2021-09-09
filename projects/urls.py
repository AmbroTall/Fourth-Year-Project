from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, UpdateProjectView, DeleteProjectView

app_name='projectss'
urlpatterns = [
    path('', ProjectListView, name='project_home'),
    path('create/', ProjectCreateView.as_view(), name='create_project'),
    path('<str:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<str:slug>/update', UpdateProjectView.as_view(), name='update_project'),
    path('<str:slug>/delete', DeleteProjectView.as_view(), name='delete_project'),


]