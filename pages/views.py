from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        # If the user is authenticated, redirect to the article list page
        if request.user.is_authenticated:
            return redirect("article_list")
        return super().dispatch(request, *args, **kwargs)


class ObjectFlashcardsView(TemplateView):
    template_name = "tutorials/object_flashcards.html"


class ObjectsTutorialView(TemplateView):
    template_name = "tutorials/objects_tutorial.html"


class ObjectQuizView(TemplateView):
    template_name = "tutorials/object_quiz.html"


class TutorialPageView(TemplateView):
    template_name = "tutorials/tutorial_list.html"


class JsGptQuizView(TemplateView):
    template_name = "jsgptquiz.html"


# Create your views here.
