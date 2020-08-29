import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        points = votes[index].getText()
        hn.append({'title': title, 'link': href})
    return hn

create_custom_hn(links, votes)
