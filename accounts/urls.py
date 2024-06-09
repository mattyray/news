#root\accounts\urls.py

from django.urls import path, include
from .views import SignUpView, CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),    
    ]       