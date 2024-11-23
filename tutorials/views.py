from django.shortcuts import render
from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY  # Ensure the key is in your settings

def generate_tutorial_content(request):
    content = None
    if request.method == "POST":
        topic = request.POST.get("topic", "")
        if topic:
            # Call ChatGPT API
            try:
                response = openai.Completion.create(
                    model="text-davinci-003", 
                    prompt=f"Write a detailed tutorial on the topic: {topic}.",
                    max_tokens=600,
                    temperature=0.7
                )
                content = response.choices[0].text.strip()
            except Exception as e:
                content = f"Error generating content: {e}"

    return render(request, "tutorials/generate_tutorial.html", {"content": content})
