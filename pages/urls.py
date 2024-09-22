from django.urls import path, include
from .views import HomePageView, JsGptQuizView, TutorialPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jsgptquiz/', JsGptQuizView.as_view(), name='jsgptquiz'),
    path('tutorials/', TutorialPageView.as_view(), name='tutorial'),

]