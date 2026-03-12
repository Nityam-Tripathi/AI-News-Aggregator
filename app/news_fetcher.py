import requests
import os
import hashlib

def generate_hash(title, content):
    text = (title + content).encode("utf-8")
    return hashlib.md5(text).hexdigest()

def fetch_news():
    api_key = os.getenv("NEWS_API_KEY")

    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=20&apiKey={api_key}"

    response = requests.get(url)

    data = response.json()

    return data["articles"]