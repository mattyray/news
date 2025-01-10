from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        # If the user is authenticated, redirect to the article list page
        if request.user.is_authenticated:
            return redirect("article_list")
        return super().dispatch(request, *args, **kwargs)






# Create your views here.
