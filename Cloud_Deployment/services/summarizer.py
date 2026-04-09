import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the lighter model with a separate free-tier quota
_MODEL_NAME = "gemini-2.5-flash"

def summarize_content(title: str, content: str) -> str:
    model = genai.GenerativeModel(_MODEL_NAME)

    prompt = f"""
    You are a helpful assistant.

    Summarize the following webpage content in 5-6 concise bullet points.

    Title: {title}

    Content:
    {content}
    """

    response = model.generate_content(prompt)
    return response.text