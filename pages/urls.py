from django.urls import path, include
from .views import HomePageView, JsGptQuizView, TutorialPageView, ObjectsTutorialView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jsgptquiz/', JsGptQuizView.as_view(), name='jsgptquiz'),
    path('tutorials/', TutorialPageView.as_view(), name='tutorial'),
    path('tutorials/objects/', ObjectsTutorialView.as_view(), name='objects_tutorial'),

]