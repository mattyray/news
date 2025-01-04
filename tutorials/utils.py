import openai
from django.conf import settings
import markdown

def generate_tutorial_content(topic):
    """
    Calls the OpenAI Chat API to generate a tutorial based on the provided topic.
    The content is returned in Markdown format for better presentation.
    """
    try:
        # Instantiate the OpenAI client
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Use the OpenAI Chat API
        response = client.chat.completions.create(
            model="gpt-4",  # Use GPT-4 or GPT-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Write a detailed tutorial on the topic: {topic}. Format the response in Markdown."}
            ],
            max_tokens=2500,
            temperature=0.7
        )
        # Convert Markdown to HTML for better formatting
        raw_content = response.choices[0].message.content
        return markdown.markdown(raw_content)
    except Exception as e:
        # Return the error message in case of failure
        return f"<p>Error generating content: {e}</p>"
