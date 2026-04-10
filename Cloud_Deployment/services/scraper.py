from bs4 import BeautifulSoup
import requests
import certifi


def scrape_website(url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10,
            verify=certifi.where()
        )
        response.raise_for_status()

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

    soup = BeautifulSoup(response.content, "html.parser")

    # Title extraction
    title = soup.title.string.strip() if soup.title else "No Title"

    # Extract paragraphs
    paragraphs = soup.find_all("p")
    content = " ".join([p.get_text().strip() for p in paragraphs])

    # 🔥 CRITICAL FIX: fallback if <p> fails
    if not content or len(content) < 50:
        content = soup.get_text(separator=" ", strip=True)

    # Clean + limit
    content = content.strip()[:4000]

    if not content:
        return {
            "Title": title,
            "Content": "",
            "error": "No content extracted"
        }

    return {
        "Title": title,
        "Content": content
    }