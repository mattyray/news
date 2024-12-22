import openai
from django.conf import settings

def generate_tutorial_content(topic):
    """
    Calls the OpenAI Chat API to generate a tutorial based on the provided topic.
    """
    try:
        # Instantiate the OpenAI client
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Use the updated OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo" if GPT-4 isn't available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Write a detailed tutorial on the topic: {topic}."}
            ],
            max_tokens=600,
            temperature=0.7
        )
        # Return the generated content
        return response.choices[0].message.content
    except Exception as e:
        # Return the error message in case of failure
        return f"Error generating content: {e}"
