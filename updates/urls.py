from django.urls import path
from .views import DisplayNews, NewsDetails , CreateNews, UpdateNews, DeleteNews, homepage

app_name='updates'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('news/', DisplayNews, name='news_list'),
    path('create/', CreateNews.as_view(), name='news_create'),
    path('<str:slug>/', NewsDetails.as_view(), name='news_details'),
    path('<str:slug>/Update', UpdateNews.as_view(), name='news_update'),
    path('<str:slug>/Delete', DeleteNews.as_view(), name='news_delete'),
]