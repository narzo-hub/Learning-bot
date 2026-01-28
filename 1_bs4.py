from bs4 import BeautifulSoup


with open("file_html","r") as f:
  html = f.read()
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
