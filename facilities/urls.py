from django.urls import path
from .views import FacilitiesListView, FacilitiesDetailView, FacilitiesCreateView, UpdateFacilitiesView, DeleteFacilitiesView

app_name='facilities'

urlpatterns = [
    path('', FacilitiesListView, name='facilities_home'),
    path('create/', FacilitiesCreateView.as_view(), name='create_facilities'),
    path('<str:slug>/', FacilitiesDetailView.as_view(), name='facilities_detail'),
    path('<str:slug>/update', UpdateFacilitiesView.as_view(), name='update_facilities'),
    path('<str:slug>/delete', DeleteFacilitiesView.as_view(), name='delete_facilities'),
]