from django.urls import path
from . import views

urlpatterns = [
    path("chatgpt/", chatgpt_view, name="chatgpt"),  # URL for the ChatGPT page
]
