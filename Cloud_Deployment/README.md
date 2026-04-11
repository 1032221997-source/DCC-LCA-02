# AI Content Scraper & Summarizer 

A powerful, cloud-deployable web application that extracts content from any website and generates concise, AI-powered summaries using Google's Gemini API.

## Objective
The primary goal of this project is to provide a seamless interface for users to quickly digest long-form web content. By combining robust web scraping with  Generative AI, the application converts complex web pages into manageable,bullet point summaries.

## Description
This project is built with a modern stack featuring a **FastAPI** backend and a responsive **Vanilla JS/CSS** frontend. 

**Key Features:**
- **Web Scraping:** Efficiently extracts title and text content from target URLs.
- **AI Summarization:** Utilizes Google Gemini Pro/Flash models to generate intelligent summaries.
- **Cloud Ready:** Optimized for deployment on **Vercel** or via **Docker**.
- **Modern UI:** A clean, vibrant interface with micro-interactions for a premium user experience.

---

##  File Structure

```bash
Cloud_Deployment/
├── api/
│   └── app.py            # FastAPI route handlers and API logic
├── frontend/
│   ├── index.html        # Web interface structure
│   ├── style.css         # Custom styling and animations
│   └── script.js         # Frontend logic and API integration
├── services/
│   ├── scraper.py        # Logic for extracting content from URLs
│   └── summarizer.py     # Gemini AI integration for summary generation
├── models/
│   └── models.py         # Pydantic data models for request/response
├── main.py               # Application entry point
├── DockerFile            # Containerization configuration
├── vercel.json           # Vercel deployment configuration
├── .env                  # Environment variables (API Keys)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Cloud_Deployment
   ```

2. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally:**
   ```bash
   python main.py
   # OR
   uvicorn api.app:app --reload
   ```

---

## Deployment

### Vercel
This project is configured for Vercel. Ensure you set the `GEMINI_API_KEY` in your Vercel Environment Variables.

### Docker
To run as a container:
```bash
docker build -t ai-summarizer .
docker run -p 8000:8000 --env-file .env ai-summarizer
```
