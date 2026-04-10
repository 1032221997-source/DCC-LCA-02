import os

port = int(os.environ.get("PORT", 8000))

os.system(f"uvicorn api.app:app --host 0.0.0.0 --port {port}")