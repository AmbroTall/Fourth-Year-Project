from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegisterForm


class LoginView(LoginView):
    fields = '__all__'
    template_name = 'user_auth/login_page.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('updates:homepage')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'user_auth/register_page.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('updates:homepage')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('updates:homepage')
        return super(RegisterView,self).get(*args, **kwargs)


