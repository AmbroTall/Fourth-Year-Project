from django.urls import path
from .views import LoginView,RegisterView
from django.contrib.auth.views import LogoutView

app_name='auth_user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page ='auth_user:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]