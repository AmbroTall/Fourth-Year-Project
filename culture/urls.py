from django.urls import path
from .views import CultureListView, CultureDetailView, CultureCreateView, UpdateCultureView, DeleteCultureView

app_name='culture'
urlpatterns = [
    path('', CultureListView, name='culture_home'),
    path('create/', CultureCreateView.as_view(), name='create_culture'),
    path('<str:slug>/', CultureDetailView.as_view(), name='culture_detail'),
    path('<str:slug>/update', UpdateCultureView.as_view(), name='update_culture'),
    path('<str:slug>/delete', DeleteCultureView.as_view(), name='delete_culture'),


]