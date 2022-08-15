from django.urls import path
from .views import *
from . import views

app_name = "accounts"
urlpatterns = [

    path('login/', views.userlogin, name="userlogin"),
    path('logout', views.userlogout, name='logout'),
    path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),






]