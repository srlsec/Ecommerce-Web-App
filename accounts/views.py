from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator

from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def userlogin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      #messages.success(request, 'You are now logged in')
      return redirect('store')
    else:
      #messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'user/user_login.html')

def userlogout(request):
  if request.method == 'POST':
    auth.logout(request)
    #messages.success(request, 'You are now logged out')
    return redirect('store')

class CustomerRegistrationView(CreateView):
    template_name = "user/user_register.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("accounts:userlogin")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
 
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
    
