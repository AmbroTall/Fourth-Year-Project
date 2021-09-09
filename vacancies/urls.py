from django.urls import path
from .views import HouseListView,HouseDetailView, HouseCreate,HouseUpdateForm,HouseDeleteView

app_name='vacancies'
urlpatterns = [
    path('', HouseListView, name='vacancy_home'),
    path('create/', HouseCreate.as_view(), name='vacancy_create'),
    path('<str:slug>/', HouseDetailView.as_view(), name='vacancy_detail'),
    path('<str:slug>/delete', HouseDeleteView.as_view(), name='vacancy_delete'),
    path('<str:slug>/update', HouseUpdateForm.as_view(), name='vacancy_update'),
]