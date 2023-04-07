from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView

class LoginPageView(LoginView):
  form_class = LoginForm
  template_name = 'web_site/index.html'
  def get_success_url(self) -> str:
    return reverse_lazy('home_page')
  
def home(request):
  return render(request, 'web_site/home.html')

class RegisterView(CreateView):
  form_class = RegisterForm
  template_name = 'web_site/register.html'
  success_url = reverse_lazy('index_page')
  
class RequestView(CreateView):
  form_class = RequestForm
  template_name = 'web_site/request.html'
  success_url = reverse_lazy('home_page')

class GroupRequestView(CreateView):
  form_class = GroupRequestForm
  template_name = 'web_site/gp_request.html'
  success_url = reverse_lazy('home_page')
  