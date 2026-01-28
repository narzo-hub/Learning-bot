import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

# Start URL
start_url = "https://example.com"

# Domain check
domain = urlparse(start_url).netloc

# Sets to avoid duplicates
visited = set()
to_visit = set([start_url])

headers = {"User-Agent": "Mozilla/5.0"}

while to_visit:
    url = to_visit.pop()
    if url in visited:
        continue
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        visited.add(url)
        print(url)  # Print the page link
        
        # Find all internal links
        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            # Check if link is internal
            if urlparse(link).netloc == domain and link not in visited:
                to_visit.add(link)
        
        time.sleep(1)  # polite crawling
    except Exception as e:
        print(f"Failed: {url} ({e})")
