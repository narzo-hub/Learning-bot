import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url = "https://example.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

internal_links = set()
domain = urlparse(url).netloc

for a in soup.find_all("a", href=True):
    href = a["href"]
    full_url = urljoin(url, href)
    if urlparse(full_url).netloc == domain:
        internal_links.add(full_url)

for link in internal_links:
    print(link)

print("\nTotal internal links:", len(internal_links))
