from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from services.scraper import scrape_website
from services.summarizer import summarize_content
from models.models import URLRequest, ContentRequest

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "frontend")), name="static")

@app.get("/")
def read_root():
    return FileResponse(str(BASE_DIR / "frontend" / "index.html"))

@app.post("/scrape")
def scrape(request: URLRequest):
    data = scrape_website(request.url)
    return data

@app.post("/summarize")
def summarize(request: ContentRequest):
    summary = summarize_content(request.title, request.content)
    return {"summary": summary}

#combined flow....(Scrape+summmarize)
@app.post("/process")
def process(request: URLRequest):
    print("STEP 1: Request received")

    try:
        scraped = scrape_website(request.url)
        print("STEP 2: Scraped data:", scraped)
    except Exception as e:
        return {
            "stage": "scraping",
            "error": str(e)
        }

    # Validate scraped structure
    if not isinstance(scraped, dict):
        return {
            "stage": "scraping",
            "error": "Invalid scrape response"
        }

    if "error" in scraped:
        return {
            "stage": "scraping",
            "error": scraped["error"]
        }

    # Handle key mismatches safely
    title = scraped.get("Title") or scraped.get("title", "No title")
    content = scraped.get("Content") or scraped.get("content", "")

    if not content:
        return {
            "stage": "scraping",
            "error": "No content extracted"
        }

    print("STEP 3: Content ready for summarization")

    try:
        summary = summarize_content(title, content)
        print("STEP 4: Summary generated")
    except Exception as e:
        return {
            "stage": "summarization",
            "error": str(e)
        }

    return {
        "title": title,
        "content": content
    }
