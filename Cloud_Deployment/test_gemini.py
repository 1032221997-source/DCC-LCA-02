import os
import traceback
from dotenv import load_dotenv

load_dotenv()

from services.summarizer import summarize_content

try:
    print("Testing with API Key length:", len(os.getenv("GEMINI_API_KEY", "")))
    summary = summarize_content("Wikipedia AI", "Artificial intelligence is intelligence demonstrated by machines.")
    print("SUCCESS! Output length:", len(summary))
except Exception as e:
    print("FAILED!")
    traceback.print_exc()
