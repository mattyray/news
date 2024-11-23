from django.urls import path
from . import views

urlpatterns = [
    # URL for taking a quiz for a specific unit
    path('quiz/<int:quiz_id>/take/', views.take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
]
