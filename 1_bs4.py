import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

start_url = "https://extraflix.live/vaa-vaathiyaar-2026/"
domain = urlparse(start_url).netloc

visited = set()
to_visit = [start_url]

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

while to_visit:
    current_url = to_visit.pop(0)
    if current_url in visited:
        continue

    try:
        response = requests.get(current_url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        visited.add(current_url)
        print("Visited:", current_url)

        # Find internal links
        for a in soup.find_all("a", href=True):
            link = urljoin(current_url, a["href"])
            if urlparse(link).netloc == domain and link not in visited and link not in to_visit:
                to_visit.append(link)

        time.sleep(1)  # polite crawling
    except Exception as e:
        print("Error at", current_url, e)

print("\nTotal internal pages found:", len(visited))

# Save to file
with open("extraflix_all_internal_links.txt", "w") as f:
    for link in visited:
        f.write(link + "\n")
