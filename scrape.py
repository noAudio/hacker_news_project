import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
