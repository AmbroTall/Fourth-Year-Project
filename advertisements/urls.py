from django.urls import path
from .views import DisplayAdvert, AdvertDetails, DisplayHouseAdvert,DisplayFooterAdvert

app_name='advertisements'

urlpatterns = [
    path('', DisplayAdvert.as_view(), name='advert'),
    path('advert_vacancies', DisplayHouseAdvert.as_view(), name='advert_vacancies'),
    path('advert_footer/', DisplayFooterAdvert.as_view(), name='advert_footer'),
    path('<str:slug>/', AdvertDetails.as_view(), name='advert_detail'),
]