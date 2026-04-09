from bs4 import BeautifulSoup
import requests

def scrape_website(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
     
    title = soup.title.string.strip() if soup.title else "No Title"
    paragraphs = soup.find_all("p")
    content = " ".join([p.get_text().strip() for p in paragraphs])
    content = content[:4000] #limiting the content size for gemini tokens

    return {
        "Title":title,
        "Content":content
    }
