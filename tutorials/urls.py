from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_tutorial_content, name='generate_tutorial'),
]
