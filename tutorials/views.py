from django.shortcuts import render
from .utils import generate_tutorial_content  # Utility function for OpenAI API

def generate_tutorial_view(request):
    """
    Handles the tutorial generation form submission and displays the content.
    """
    content = None
    if request.method == "POST":
        topic = request.POST.get("topic", "")
        if topic:
            # Call the utility function to generate content
            content = generate_tutorial_content(topic)

    # Render the template with the generated content
    return render(request, "tutorials/generate_tutorial.html", {"content": content})
