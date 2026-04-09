from fastapi import FastAPI
from services.scraper import scrape_website
from services.summarizer import summarize_content
from models.models import URLRequest, ContentRequest

app = FastAPI()

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
    scraped = scrape_website(request.url)
    summary = summarize_content(scraped["Title"], scraped["Content"])

    return {
        "title": scraped["Title"],
        "summary": summary
    }
