from django.urls import path, include
from .views import HomePageView, JsGptQuizView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jsgptquiz/', JsGptQuizView.as_view(), name='jsgptquiz'),

]