import requests
import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h2')

for t in titles:
    print(t.text)
